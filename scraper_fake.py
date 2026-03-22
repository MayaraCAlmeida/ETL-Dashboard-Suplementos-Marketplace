"""
Simulacao de Scraping de Precos - Suplementos

Scraping real de sites como Amazon, Mercado Livre e Shopee
pode violar termos de uso se feito sem API oficial.
"""

# simula coleta de preços de suplementos e gera CSV

import random
import pandas as pd
from datetime import datetime

produtos = [
    {"produto": "Whey Protein 900g", "categoria": "Proteina", "peso_g": 900},
    {"produto": "Creatina 300g",      "categoria": "Creatina", "peso_g": 300},
]

marcas = ["Soldiers Nutrition", "Max Titanium", "Integral Medica",
          "DUX", "Dark Lab", "Black Skull"]

dados = []
for _ in range(120):
    item  = random.choice(produtos)
    preco = round(random.uniform(119.90, 249.90) if item["produto"] == "Whey Protein 900g"
                  else random.uniform(79.90, 179.90), 2)

    dados.append({
        "produto":     item["produto"],
        "categoria":   item["categoria"],
        "marca":       random.choice(marcas),
        "peso_g":      item["peso_g"],
        "preco":       preco,
        "estoque":     random.randint(0, 400),
        "data_coleta": datetime.now().strftime("%Y-%m-%d"),
    })

df = pd.DataFrame(dados)
df.to_csv("vendas_suplementos.csv", index=False, encoding="utf-8")
