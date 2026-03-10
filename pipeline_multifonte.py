"""
Simulação de Pipeline de Scraping Multifonte — Suplementos

Este script simula a coleta de preços e estoque de suplementos
a partir de diferentes fontes de e-commerce (dados fictícios).

Fontes simuladas:
- E-commerce genérico
- Mercado Livre
- Amazon
- Shopee

Objetivo:
Gerar um dataset unificado e pronto para análises em Data Analytics
ou visualizações em Power BI.

⚠️ Observação:
Scraping real de marketplaces pode violar termos de uso
quando feito sem API oficial.
"""

import pandas as pd
from datetime import datetime

# =========================
# 1. SCRAPING FICTÍCIO
# =========================
scraping_ficticio = [
    {
        "produto": "Whey Protein 900g DUX",
        "marca": "DUX",
        "preco": 229.90,
        "estoque": 180,
        "fonte": "E-commerce Fictício",
    },
    {
        "produto": "Creatina 300g Max Titanium",
        "marca": "Max Titanium",
        "preco": 139.90,
        "estoque": 250,
        "fonte": "E-commerce Fictício",
    },
]

# =========================
# 2. MERCADO LIVRE (SIMULADO)
# =========================
mercado_livre = [
    {
        "produto": "Whey Protein 900g Black Skull",
        "marca": "Black Skull",
        "preco": 199.90,
        "estoque": 200,
        "fonte": "Mercado Livre",
    },
    {
        "produto": "Creatina 300g Dark Lab",
        "marca": "Dark Lab",
        "preco": 129.90,
        "estoque": 90,
        "fonte": "Mercado Livre",
    },
]

# =========================
# 3. AMAZON (SIMULADO)
# =========================
amazon = [
    {
        "produto": "Whey Protein 900g Integral Médica",
        "marca": "Integral Médica",
        "preco": 219.90,
        "estoque": 140,
        "fonte": "Amazon",
    },
    {
        "produto": "Creatina 300g Soldiers Nutrition",
        "marca": "Soldiers Nutrition",
        "preco": 134.90,
        "estoque": 110,
        "fonte": "Amazon",
    },
]

# =========================
# 4. SHOPEE (SIMULADO)
# =========================
shopee = [
    {
        "produto": "Whey Protein 900g Max Titanium",
        "marca": "Max Titanium",
        "preco": 179.90,
        "estoque": 300,
        "fonte": "Shopee",
    },
    {
        "produto": "Creatina 300g Black Skull",
        "marca": "Black Skull",
        "preco": 119.90,
        "estoque": 160,
        "fonte": "Shopee",
    },
]

# =========================
# 5. UNIFICAR TODAS AS FONTES
# =========================
dados_unificados = scraping_ficticio + mercado_livre + amazon + shopee

df = pd.DataFrame(dados_unificados)

# =========================
# 6. PADRONIZAÇÃO FINAL
# =========================
df["data_coleta"] = datetime.now().strftime("%Y-%m-%d")
df["marca"] = df["marca"].str.upper()
df["produto"] = df["produto"].str.lower()

# =========================
# 7. COLUNAS ANALÍTICAS
# =========================
df["valor_estoque"] = df["preco"] * df["estoque"]

# =========================
# 8. EXPORTAR DATASET FINAL
# =========================
arquivo_saida = "dataset_suplementos_multifonte.csv"
df.to_csv(arquivo_saida, index=False, encoding="utf-8")

print(f"Dataset multifonte gerado com sucesso: {arquivo_saida}")
