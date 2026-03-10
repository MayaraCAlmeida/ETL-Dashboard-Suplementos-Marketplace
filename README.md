# Suplementos Multi-Marketplace Analytics

Pipeline completo de coleta, tratamento e visualizacao de dados de suplementos (Creatina e Whey Protein) nos marketplaces Amazon, Mercado Livre e Shopee.

---

## Estrutura do Projeto

```
.
├── scraper_fake.py                     # Geracao de dados ficticios de scraping
├── coleta_marketplace_simulada.py      # Coleta simulada via API ficticia (multi-marketplace)
├── pipeline_multifonte.py              # Unificacao de dados de multiplas fontes
├── limpeza_dados.py                    # Limpeza e padronizacao do dataset
├── import_PostgreSQL.py                # Carga dos dados no PostgreSQL
├── sqlmarketplace_pipeline.sql         # Criacao de tabelas, views e indices no banco
├── utils.py                            # Funcoes auxiliares de tratamento de texto
├── Medidas_DAX.md                      # Medidas DAX para uso no Power BI
├── dados.csv                           # Dataset de exemplo
├── Dashboard-analitico.pbix            # Dashboard analitico no Power BI
├── Dashboard-impacto.pbix              # Dashboard de impacto no Power BI
├── .env.example                        # Modelo de variaveis de ambiente
└── .gitignore
```

---

## Fluxo do Pipeline

```
scraper_fake.py / coleta_marketplace_simulada.py
              |
              v
    pipeline_multifonte.py  (unificacao)
              |
              v
      limpeza_dados.py  (tratamento)
              |
              v
    import_PostgreSQL.py  (carga)
              |
              v
  sqlmarketplace_pipeline.sql  (views e KPIs)
              |
              v
    Power BI (Dashboards)
```

---

## Configuracao

### Variaveis de Ambiente

Copie o arquivo `.env.example` e preencha com suas credenciais:

```bash
cp .env.example .env
```

Variaveis esperadas:

| Variavel      | Descricao                  | Padrao     |
|---------------|----------------------------|------------|
| `DB_USER`     | Usuario do PostgreSQL       | `postgres` |
| `DB_PASSWORD` | Senha do banco              | obrigatorio |
| `DB_HOST`     | Host do banco               | `localhost` |
| `DB_PORT`     | Porta do banco              | `5432`     |
| `DB_NAME`     | Nome do banco de dados      | `Suplementos` |

### Dependencias Python

```bash
pip install pandas sqlalchemy psycopg2-binary
```

---

## Como Executar

**1. Gerar dados simulados**

```bash
python coleta_marketplace_simulada.py
# ou
python scraper_fake.py
```

**2. Unificar fontes**

```bash
python pipeline_multifonte.py
```

**3. Limpar e padronizar**

```bash
python limpeza_dados.py
```

**4. Carregar no PostgreSQL**

```bash
python import_PostgreSQL.py
```

**5. Criar views e indices no banco**

Execute o arquivo `sqlmarketplace_pipeline.sql` no seu cliente PostgreSQL (ex: psql, DBeaver, pgAdmin).

---

## Dados

### Marketplaces cobertos

- Amazon
- Mercado Livre
- Shopee

### Produtos analisados

- Creatina 300g
- Whey Protein 900g

### Marcas incluidas

- Soldiers Nutrition
- Max Titanium
- Integral Medica
- DUX
- Dark Lab
- Black Skull

### Campos do dataset

| Campo              | Tipo      | Descricao                        |
|--------------------|-----------|----------------------------------|
| `marketplace`      | texto     | Nome do marketplace              |
| `produto`          | texto     | Categoria do produto             |
| `marca`            | texto     | Marca do produto                 |
| `peso_g`           | inteiro   | Peso em gramas                   |
| `preco`            | decimal   | Preco de venda                   |
| `vendas_estimadas` | inteiro   | Volume de vendas estimado        |
| `avaliacao`        | decimal   | Nota media do produto            |
| `num_avaliacoes`   | inteiro   | Numero total de avaliacoes       |
| `data_coleta`      | data      | Data de coleta do dado           |

---

## KPIs e Visualizacoes

As medidas DAX em `Medidas_DAX.md` incluem:

- Receita Total e Projetada (+5%)
- Total de Vendas e Meta (+10%)
- Preco Medio e Meta (-2%)
- Avaliacao Media Ponderada por numero de avaliacoes

Os dashboards Power BI consomem a view `vw_coleta_geral` gerada no banco.

---

## Observacoes

O scraping real de marketplaces como Amazon, Mercado Livre e Shopee pode violar os termos de uso dessas plataformas quando realizado sem API oficial. Este projeto utiliza exclusivamente dados ficticios para fins de estudo e demonstracao.
