# simula coleta de preços de múltiplos marketplaces e gera CSV
# Fontes simuladas:
#- E-commerce genérico
#- Mercado Livre
#- Amazon
#- Shopee

import pandas as pd
from datetime import datetime

scraping_ficticio = [
    {"produto": "Whey Protein 900g DUX",          "marca": "DUX",          "preco": 229.90, "estoque": 180, "fonte": "E-commerce Fictício"},
    {"produto": "Creatina 300g Max Titanium",      "marca": "Max Titanium", "preco": 139.90, "estoque": 250, "fonte": "E-commerce Fictício"},
]

mercado_livre = [
    {"produto": "Whey Protein 900g Black Skull",   "marca": "Black Skull",  "preco": 199.90, "estoque": 200, "fonte": "Mercado Livre"},
    {"produto": "Creatina 300g Dark Lab",           "marca": "Dark Lab",     "preco": 129.90, "estoque": 90,  "fonte": "Mercado Livre"},
]

amazon = [
    {"produto": "Whey Protein 900g Integral Médica", "marca": "Integral Médica",    "preco": 219.90, "estoque": 140, "fonte": "Amazon"},
    {"produto": "Creatina 300g Soldiers Nutrition",  "marca": "Soldiers Nutrition", "preco": 134.90, "estoque": 110, "fonte": "Amazon"},
]

shopee = [
    {"produto": "Whey Protein 900g Max Titanium",  "marca": "Max Titanium", "preco": 179.90, "estoque": 300, "fonte": "Shopee"},
    {"produto": "Creatina 300g Black Skull",        "marca": "Black Skull",  "preco": 119.90, "estoque": 160, "fonte": "Shopee"},
]

df = pd.DataFrame(scraping_ficticio + mercado_livre + amazon + shopee)

df["data_coleta"]   = datetime.now().strftime("%Y-%m-%d")
df["marca"]         = df["marca"].str.upper()
df["produto"]       = df["produto"].str.lower()
df["valor_estoque"] = df["preco"] * df["estoque"]

df.to_csv("dataset_suplementos_multifonte.csv", index=False, encoding="utf-8")
