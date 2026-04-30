import pandas as pd
from sqlalchemy import create_engine
import click

dtype = {
    "tournament": "string",
    "date": "string",
    "series": "string",
    "court": "string",
    "surface": "string",
    "round": "string",
    "BestOf": "Int64",
    "player1": "string",
    "player2": "string",
    "winner": "string",
    "rank1": "Int64",
    "rank2": "Int64",
    "pts1": "Int64",
    "pts2": "Int64",
    "odds1": "Float64",
    "odds2": "Float64",
    "score": "string"
}

parse_dates = [
    "Date"
]


@click.command()
@click.option('--filename', default='atp_tennis.csv', help='CSV file name')
@click.option('--table-name', default='tenis_data', help='Table name')
@click.option('--chunksize', default=5000, type=int, help='Chunk size')
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='tenis_data', help='PostgreSQL database')
def run(filename, table_name, chunksize, pg_user, pg_pass, pg_host, pg_port, pg_db):

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    df_iter = pd.read_csv(
    filename,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=chunksize
    )
    all_chunks = []

    for chunk in df_iter:
        chunk['Odd_1'] = pd.to_numeric(chunk['Odd_1'], errors='coerce')
        chunk['Odd_2'] = pd.to_numeric(chunk['Odd_2'], errors='coerce')


        chunk['Date'] = pd.to_datetime(chunk['Date'], errors='coerce')

        chunk = chunk[
            (chunk['Date'] >= '2015-01-01') & 
            (chunk['Odd_1'] > 0) & 
            (chunk['Odd_2'] > 0)
        ].copy()

        chunk['target'] = (chunk['Player_1'] == chunk['Winner']).astype(int)

        all_chunks.append(chunk)
        print('listo')

    df_final = pd.concat(all_chunks).sort_values('Date').reset_index(drop=True)


    print("--- Validación de Límites ---")
    print(f"Fecha mínima encontrada: {df_final['Date'].max()}")
    print(f"Cuota mínima Odd_1: {df_final['Odd_1'].min()}")
    print(f"Cuota mínima Odd_2: {df_final['Odd_2'].min()}")

    # Subida directa
    df_final.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace', # 'replace' crea la tabla de nuevo; 'append' añade datos
        index=False,         # No guardamos el índice de pandas como columna
        method='multi',      # CRITICO: Agrupa filas para insertar más rápido
        chunksize=chunksize     # Pandas divide el DF en pedazos al enviarlo a SQL
    )

    print(f"¡Éxito! Se han subido {len(df_final)} filas a la tabla '{table_name}'.")


if __name__ == '__main__':
    run() 