"""
Simulacao de Scraping de Precos - Suplementos

Este script gera um dataset ficticio simulando a coleta de precos
de suplementos (ex: Whey Protein e Creatina) em e-commerces.


Observacao:
Scraping real de sites como Amazon, Mercado Livre e Shopee
pode violar termos de uso se feito sem API oficial.
"""

import pandas as pd
import random
from datetime import datetime

# ---------------------------------
# Produtos e marcas (dados ficticios)
# ---------------------------------

produtos = [
    {"produto": "Whey Protein 900g", "categoria": "Proteina", "peso_g": 900},
    {"produto": "Creatina 300g", "categoria": "Creatina", "peso_g": 300},
]

marcas = [
    "Soldiers Nutrition",
    "Max Titanium",
    "Integral Medica",
    "DUX",
    "Dark Lab",
    "Black Skull",
]

# ---------------------------------
# Simulacao de scraping
# ---------------------------------

dados = []

for _ in range(120):  # quantidade de registros simulados
    item = random.choice(produtos)

    # Precos ficticios realistas
    if item["produto"] == "Whey Protein 900g":
        preco = round(random.uniform(119.90, 249.90), 2)
    else:
        preco = round(random.uniform(79.90, 179.90), 2)

    dados.append(
        {
            "produto": item["produto"],
            "categoria": item["categoria"],
            "marca": random.choice(marcas),
            "peso_g": item["peso_g"],
            "preco": preco,
            "estoque": random.randint(0, 400),
            "data_coleta": datetime.now().strftime("%Y-%m-%d"),
        }
    )

# ---------------------------------
# Criando DataFrame
# ---------------------------------

df = pd.DataFrame(dados)

# ---------------------------------
# Salvando CSV
# ---------------------------------

arquivo_saida = "vendas_suplementos.csv"
df.to_csv(arquivo_saida, index=False, encoding="utf-8")

print(f"Arquivo '{arquivo_saida}' gerado com sucesso")