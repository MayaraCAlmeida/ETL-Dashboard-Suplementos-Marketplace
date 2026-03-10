"""
load_to_postgres.py

Pipeline de carga de dados para PostgreSQL.

Este script realiza a importação do arquivo CSV contendo dados
simulados de suplementos (marketplaces, preços, vendas, avaliações etc.)
e insere os registros em uma tabela dentro de um banco PostgreSQL.

Etapas executadas:
1. Validação do arquivo CSV
2. Leitura do dataset
3. Visualização inicial dos dados
4. Conexão com PostgreSQL via SQLAlchemy
5. Criação/Substituição da tabela
6. Inserção completa dos registros

Observação:
As credenciais do banco devem ser configuradas via variáveis de ambiente.
"""

import os
import pandas as pd
from sqlalchemy import create_engine


# =========================
# 1. Conexão com PostgreSQL
# =========================


def conectar_postgres():
    """
    Cria e retorna uma engine de conexão com PostgreSQL
    usando variáveis de ambiente.

    Variáveis esperadas:
    - DB_USER
    - DB_PASSWORD
    - DB_HOST
    - DB_PORT
    - DB_NAME
    """

    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    database = os.getenv("DB_NAME", "Suplementos")

    if not password:
        raise ValueError(" A variável de ambiente DB_PASSWORD não foi definida.")

    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    return create_engine(url)


# =========================
# 2. Função Principal
# =========================


def carregar_csv_para_postgres(
    caminho_csv: str, tabela: str = "coleta", modo: str = "replace"
):
    """
    Lê um arquivo CSV e carrega os dados em uma tabela PostgreSQL.

    Parâmetros
    ----------
    caminho_csv : str
        Caminho do arquivo CSV.
    tabela : str
        Nome da tabela destino no banco.
    modo : str
        Define o comportamento caso a tabela já exista:
        - "replace" → recria a tabela do zero
        - "append"  → adiciona novos registros
    """

    print(" Iniciando pipeline de carga...\n")

    # 1. Validar arquivo
    if not os.path.exists(caminho_csv):
        raise FileNotFoundError(f" Arquivo CSV não encontrado: {caminho_csv}")

    # 2. Ler CSV
    print(" Lendo arquivo CSV...")
    df = pd.read_csv(caminho_csv)

    print("\n Dataset carregado com sucesso!")
    print(" Primeiras linhas:")
    print(df.head())

    print("\n Total de registros:", len(df))

    # 3. Conectar ao banco
    print("\n Conectando ao PostgreSQL...")
    engine = conectar_postgres()

    # 4. Inserir dados
    print(f"\n Inserindo dados na tabela '{tabela}' (modo = {modo})...")

    df.to_sql(name=tabela, con=engine, if_exists=modo, index=False)

    print(f"\n Pipeline finalizado!")
    print(f" Dados carregados com sucesso na tabela '{tabela}'.")


# =========================
# 3. Execução Direta
# =========================

if __name__ == "__main__":
    caminho_csv = "data/marketplace_suplementos_simulado.csv"
    carregar_csv_para_postgres(caminho_csv)
