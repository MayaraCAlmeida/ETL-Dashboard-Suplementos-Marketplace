"""
Coleta Simulada Multi-Marketplace — Suplementos

Este script simula uma coleta de dados via API fictícia,
representando preços e desempenho de vendas de suplementos
em diferentes marketplaces.

Marketplaces simulados:
- Amazon
- Mercado Livre
- Shopee

Produtos analisados:
- Creatina 300g
- Whey Protein 900g

Dataset gerado:
Inclui preço, vendas estimadas, avaliações e número de reviews.

Observação:
Scraping ou coleta real de marketplaces deve ser feita
preferencialmente via APIs oficiais.
"""

import pandas as pd

# =========================
# Data de coleta
# =========================
data_coleta = "2026-01-26"

# =========================
# Dados simulados (API fictícia)
# =========================
dados = [
    [
        "Amazon",
        "Creatina",
        "Soldiers Nutrition",
        300,
        79.9,
        1800,
        4.7,
        4200,
        data_coleta,
    ],
    ["Amazon", "Creatina", "Max Titanium", 300, 89.9, 2200, 4.8, 9800, data_coleta],
    ["Amazon", "Creatina", "Integral Medica", 300, 85.9, 2000, 4.7, 7600, data_coleta],
    ["Amazon", "Creatina", "DUX", 300, 99.9, 1600, 4.9, 5100, data_coleta],
    ["Amazon", "Creatina", "Dark Lab", 300, 74.9, 2500, 4.6, 6900, data_coleta],
    ["Amazon", "Creatina", "Black Skull", 300, 69.9, 2800, 4.5, 8300, data_coleta],
    [
        "Mercado Livre",
        "Creatina",
        "Soldiers Nutrition",
        300,
        76.9,
        5200,
        4.7,
        3100,
        data_coleta,
    ],
    [
        "Mercado Livre",
        "Creatina",
        "Max Titanium",
        300,
        87.9,
        6800,
        4.8,
        8700,
        data_coleta,
    ],
    [
        "Mercado Livre",
        "Creatina",
        "Integral Medica",
        300,
        82.9,
        6100,
        4.7,
        6400,
        data_coleta,
    ],
    ["Mercado Livre", "Creatina", "DUX", 300, 97.9, 4500, 4.9, 5200, data_coleta],
    ["Mercado Livre", "Creatina", "Dark Lab", 300, 72.9, 7400, 4.6, 5900, data_coleta],
    [
        "Mercado Livre",
        "Creatina",
        "Black Skull",
        300,
        67.9,
        8200,
        4.5,
        7600,
        data_coleta,
    ],
    [
        "Shopee",
        "Creatina",
        "Soldiers Nutrition",
        300,
        74.9,
        6100,
        4.6,
        2800,
        data_coleta,
    ],
    ["Shopee", "Creatina", "Max Titanium", 300, 85.9, 7200, 4.8, 6900, data_coleta],
    ["Shopee", "Creatina", "Integral Medica", 300, 80.9, 6600, 4.7, 5400, data_coleta],
    ["Shopee", "Creatina", "DUX", 300, 95.9, 4900, 4.9, 4100, data_coleta],
    ["Shopee", "Creatina", "Dark Lab", 300, 70.9, 8800, 4.6, 6300, data_coleta],
    ["Shopee", "Creatina", "Black Skull", 300, 65.9, 9500, 4.5, 7900, data_coleta],
    [
        "Amazon",
        "Whey Protein",
        "Soldiers Nutrition",
        900,
        109.9,
        1400,
        4.6,
        3900,
        data_coleta,
    ],
    [
        "Amazon",
        "Whey Protein",
        "Max Titanium",
        900,
        119.9,
        2100,
        4.8,
        10200,
        data_coleta,
    ],
    [
        "Amazon",
        "Whey Protein",
        "Integral Medica",
        900,
        115.9,
        1900,
        4.7,
        8800,
        data_coleta,
    ],
    ["Amazon", "Whey Protein", "DUX", 900, 149.9, 1300, 4.9, 6200, data_coleta],
    ["Amazon", "Whey Protein", "Dark Lab", 900, 104.9, 2300, 4.6, 7100, data_coleta],
    ["Amazon", "Whey Protein", "Black Skull", 900, 99.9, 2600, 4.5, 8600, data_coleta],
    [
        "Mercado Livre",
        "Whey Protein",
        "Soldiers Nutrition",
        900,
        106.9,
        4800,
        4.6,
        3400,
        data_coleta,
    ],
    [
        "Mercado Livre",
        "Whey Protein",
        "Max Titanium",
        900,
        117.9,
        6500,
        4.8,
        9100,
        data_coleta,
    ],
    [
        "Mercado Livre",
        "Whey Protein",
        "Integral Medica",
        900,
        112.9,
        6100,
        4.7,
        7800,
        data_coleta,
    ],
    ["Mercado Livre", "Whey Protein", "DUX", 900, 147.9, 4200, 4.9, 6900, data_coleta],
    [
        "Mercado Livre",
        "Whey Protein",
        "Dark Lab",
        900,
        102.9,
        7200,
        4.6,
        8300,
        data_coleta,
    ],
    [
        "Mercado Livre",
        "Whey Protein",
        "Black Skull",
        900,
        97.9,
        7900,
        4.5,
        9600,
        data_coleta,
    ],
    [
        "Shopee",
        "Whey Protein",
        "Soldiers Nutrition",
        900,
        104.9,
        5600,
        4.6,
        3100,
        data_coleta,
    ],
    [
        "Shopee",
        "Whey Protein",
        "Max Titanium",
        900,
        115.9,
        6900,
        4.8,
        8400,
        data_coleta,
    ],
    [
        "Shopee",
        "Whey Protein",
        "Integral Medica",
        900,
        110.9,
        6400,
        4.7,
        7200,
        data_coleta,
    ],
    ["Shopee", "Whey Protein", "DUX", 900, 145.9, 4500, 4.9, 5800, data_coleta],
    ["Shopee", "Whey Protein", "Dark Lab", 900, 100.9, 8600, 4.6, 9100, data_coleta],
    ["Shopee", "Whey Protein", "Black Skull", 900, 95.9, 9200, 4.5, 10400, data_coleta],
]

# =========================
# Criar DataFrame
# =========================
colunas = [
    "marketplace",
    "produto",
    "marca",
    "peso_g",
    "preco",
    "vendas_estimadas",
    "avaliacao",
    "num_avaliacoes",
    "data_coleta",
]

df = pd.DataFrame(dados, columns=colunas)

# =========================
# Salvar CSV
# =========================
arquivo_saida = "marketplace_suplementos_simulado.csv"
df.to_csv(arquivo_saida, index=False, encoding="utf-8")

print(f"Coleta simulada multi-marketplace gerada com sucesso: {arquivo_saida}")
