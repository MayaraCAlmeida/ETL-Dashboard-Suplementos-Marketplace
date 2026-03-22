# sobe CSV de suplementos pro postgres

import os
import pandas as pd
from sqlalchemy import create_engine


def conectar_postgres():
    password = os.getenv("DB_PASSWORD")
    if not password:
        raise ValueError("DB_PASSWORD não definida")

    return create_engine(
        f"postgresql://{os.getenv('DB_USER', 'postgres')}:{password}"
        f"@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}"
        f"/{os.getenv('DB_NAME', 'Suplementos')}"
    )


def carregar_csv_para_postgres(caminho_csv, tabela="coleta", modo="replace"):
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f"arquivo não encontrado: {caminho_csv}")

    df = pd.read_csv(caminho_csv)
    print(df.head())
    print(f"{len(df)} registros")

    engine = conectar_postgres()
    df.to_sql(name=tabela, con=engine, if_exists=modo, index=False)
    print(f"tabela '{tabela}' atualizada")


if __name__ == "__main__":
    carregar_csv_para_postgres("data/marketplace_suplementos_simulado.csv")
