# limpeza e padronização do dataset de suplementos

import pandas as pd

df = pd.read_csv("vendas_suplementos.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

colunas_texto = df.select_dtypes(include="object").columns
df[colunas_texto] = df[colunas_texto].apply(lambda x: x.str.strip())

df["produto"] = df["produto"].str.lower()
df["marca"]   = df["marca"].str.upper()

df["estoque"] = df["estoque"].fillna(0)
df["preco"]   = df["preco"].fillna(0)

df["data_coleta"] = pd.to_datetime(df["data_coleta"], errors="coerce")

df = df.drop_duplicates()

df["valor_estoque"] = df["preco"] * df["estoque"]

df.to_csv("vendas_suplementos_limpo.csv", index=False)
