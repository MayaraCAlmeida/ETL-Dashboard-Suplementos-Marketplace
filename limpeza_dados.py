"""
Pipeline de Limpeza e Tratamento de Dados — Suplementos

Este script realiza o processo de limpeza e padronização
de um dataset fictício de vendas de suplementos.

Etapas aplicadas:
- Padronização de nomes de colunas
- Limpeza de textos
- Tratamento de valores nulos
- Conversão de tipos
- Remoção de duplicatas
- Criação de coluna analítica (valor total em estoque)

Saída final:
Arquivo CSV pronto para análise e dashboards no Power BI.
"""

import pandas as pd

# =========================
# 1. Carregar dados brutos
# =========================
df = pd.read_csv("vendas_suplementos.csv")

# =========================
# 2. Padronizar nomes das colunas
# =========================
df.columns = (
    df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
)

# =========================
# 3. Limpar colunas de texto
# =========================
colunas_texto = df.select_dtypes(include="object").columns
df[colunas_texto] = df[colunas_texto].apply(lambda x: x.str.strip())

# =========================
# 4. Padronização semântica
# =========================
df["produto"] = df["produto"].str.lower()
df["marca"] = df["marca"].str.upper()

# =========================
# 5. Tratamento de valores nulos
# =========================
df["estoque"] = df["estoque"].fillna(0)
df["preco"] = df["preco"].fillna(0)

# =========================
# 6. Conversão de tipos
# =========================
df["data_coleta"] = pd.to_datetime(df["data_coleta"], errors="coerce")

# =========================
# 7. Remover duplicatas
# =========================
df = df.drop_duplicates()

# =========================
# 8. Criar colunas analíticas
# =========================
df["valor_estoque"] = df["preco"] * df["estoque"]

# =========================
# 9. Exportar dataset limpo
# =========================
arquivo_saida = "vendas_suplementos_limpo.csv"
df.to_csv(arquivo_saida, index=False)

print(f"Dados limpos e prontos para análise: {arquivo_saida}")
