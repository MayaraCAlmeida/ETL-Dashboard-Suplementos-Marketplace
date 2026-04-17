# Suplementos Multi-Marketplace Analytics

## Visão Geral

Pipeline completo de coleta, tratamento e visualização de dados de suplementos (Creatina e Whey Protein) nos marketplaces Amazon, Mercado Livre e Shopee. O projeto cobre geração de dados simulados, unificação de múltiplas fontes, limpeza, carga no PostgreSQL e dashboards analíticos no Power BI.

> Os marketplaces reais podem ter políticas restritivas para scraping. Este projeto utiliza exclusivamente dados fictícios para fins de estudo e demonstração.

### Marketplaces e Produtos Cobertos

| Marketplace | Produtos | Marcas |
|---|---|---|
| Amazon | Creatina 300g, Whey Protein 900g | Soldiers Nutrition, Max Titanium, Integral Medica, DUX, Dark Lab, Black Skull |
| Mercado Livre | Creatina 300g, Whey Protein 900g | Soldiers Nutrition, Max Titanium, Integral Medica, DUX, Dark Lab, Black Skull |
| Shopee | Creatina 300g, Whey Protein 900g | Soldiers Nutrition, Max Titanium, Integral Medica, DUX, Dark Lab, Black Skull |

---

## Estrutura do Projeto

```plaintext
.
├── scraper_fake.py                     # Geração de dados fictícios de scraping
├── coleta_marketplace_simulada.py      # Coleta simulada via API fictícia (multi-marketplace)
├── pipeline_multifonte.py              # Unificação de dados de múltiplas fontes
├── limpeza_dados.py                    # Limpeza e padronização do dataset
├── import_PostgreSQL.py                # Carga dos dados no PostgreSQL
├── sqlmarketplace_pipeline.sql         # Criação de tabelas, views e índices no banco
├── utils.py                            # Funções auxiliares de tratamento de texto
├── Medidas_DAX.md                      # Medidas DAX para uso no Power BI
├── dados.csv                           # Dataset de exemplo
├── Dashboard-analitico.pbix            # Dashboard analítico no Power BI
├── Dashboard-impacto.pbix              # Dashboard de impacto no Power BI
├── .env.example                        # Modelo de variáveis de ambiente
└── .gitignore
```

---

## Fluxo do Pipeline

```
scraper_fake.py / coleta_marketplace_simulada.py
                        │
                        ▼
           pipeline_multifonte.py
              (unificação de fontes)
                        │
                        ▼
              limpeza_dados.py
           (limpeza e padronização)
                        │
                        ▼
            import_PostgreSQL.py
                  (carga)
                        │
                        ▼
        sqlmarketplace_pipeline.sql
           (views, KPIs e índices)
                        │
                        ▼
              Power BI (Dashboards)
```

### Etapas

**1. Coleta (`scraper_fake.py` / `coleta_marketplace_simulada.py`)**
Geração de dados simulados de scraping para os três marketplaces, cobrindo preços, avaliações e volume de vendas estimado por produto e marca.

**2. Unificação (`pipeline_multifonte.py`)**
Consolidação dos dados de múltiplas fontes em um dataset único, com padronização de schema entre os marketplaces.

**3. Limpeza (`limpeza_dados.py`)**
Tratamento de nulos, padronização de nomes de marcas e produtos via `utils.py`, conversão de tipos e remoção de registros inconsistentes.

**4. Carga (`import_PostgreSQL.py`)**
Importação do dataset limpo para o PostgreSQL via SQLAlchemy.

**5. Views e KPIs (`sqlmarketplace_pipeline.sql`)**
Criação de tabelas, índices e da view `vw_coleta_geral`, que alimenta diretamente os dashboards no Power BI.

**6. Dashboards (`Dashboard-analitico.pbix` / `Dashboard-impacto.pbix`)**
Visualizações com medidas DAX cobrindo receita, vendas, preço médio e avaliação ponderada.

---

## Modelo de Dados

| Campo | Tipo | Descrição |
|---|---|---|
| `marketplace` | texto | Nome do marketplace |
| `produto` | texto | Categoria do produto |
| `marca` | texto | Marca do produto |
| `peso_g` | inteiro | Peso em gramas |
| `preco` | decimal | Preço de venda |
| `vendas_estimadas` | inteiro | Volume de vendas estimado |
| `avaliacao` | decimal | Nota média do produto |
| `num_avaliacoes` | inteiro | Número total de avaliações |
| `data_coleta` | data | Data de coleta do dado |

---

## KPIs e Visualizações

As medidas DAX em `Medidas_DAX.md` incluem:

- Receita Total e Projetada (+5%)
- Total de Vendas e Meta (+10%)
- Preço Médio e Meta (-2%)
- Avaliação Média Ponderada por número de avaliações

Todos os dashboards consomem a view `vw_coleta_geral` gerada no banco.

---

## Como Executar

### Pré-requisitos

- Python 3.9+
- PostgreSQL rodando localmente ou em nuvem

```bash
pip install pandas sqlalchemy psycopg2-binary
```

### 1. Configurar o banco de dados

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

| Variável | Descrição | Padrão |
|---|---|---|
| `DB_USER` | Usuário do PostgreSQL | `postgres` |
| `DB_PASSWORD` | Senha do banco | obrigatório |
| `DB_HOST` | Host do banco | `localhost` |
| `DB_PORT` | Porta do banco | `5432` |
| `DB_NAME` | Nome do banco de dados | `Suplementos` |

### 2. Executar o pipeline

```bash
# 1. Gerar dados simulados
python coleta_marketplace_simulada.py
# ou
python scraper_fake.py

# 2. Unificar fontes
python pipeline_multifonte.py

# 3. Limpar e padronizar
python limpeza_dados.py

# 4. Carregar no PostgreSQL
python import_PostgreSQL.py
```

### 3. Criar views e índices no banco

Execute o arquivo `sqlmarketplace_pipeline.sql` no seu cliente PostgreSQL (psql, DBeaver ou pgAdmin).

### 4. Power BI

Abra `Dashboard-analitico.pbix` ou `Dashboard-impacto.pbix` no Power BI Desktop. As medidas DAX estão documentadas em `Medidas_DAX.md`.

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| `pandas` | Manipulação e limpeza dos dados |
| `sqlalchemy` + `psycopg2` | Conexão e carga no PostgreSQL |
| PostgreSQL | Armazenamento, views e KPIs |
| Power BI (DAX) | Dashboards analíticos |

---

## Responsável Técnica

Desenvolvido por: **Mayara C. Almeida** | Analista de Dados
