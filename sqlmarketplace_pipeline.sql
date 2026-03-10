/*
===========================================================
Projeto: Suplementos Multi-Marketplace Analytics
Banco: PostgreSQL

Este arquivo contém:

- Criação da tabela principal (coleta)
- Views analíticas para Power BI
- Índices para otimização
- Consultas KPI para insights de negócio
===========================================================
*/


-- =========================================================
-- 1. Verificar existência da tabela
-- =========================================================

SELECT table_name
FROM information_schema.tables
WHERE table_name = 'coleta';



-- =========================================================
-- 2. Criar tabela principal (dados simulados)
-- =========================================================

CREATE TABLE IF NOT EXISTS coleta (
    id SERIAL PRIMARY KEY,
    marketplace VARCHAR(50),
    produto VARCHAR(100),
    marca VARCHAR(100),
    peso_g INTEGER,
    preco NUMERIC(10,2),
    vendas_estimadas INTEGER,
    avaliacao NUMERIC(2,1),
    num_avaliacoes INTEGER,
    data_coleta DATE
);



-- =========================================================
-- 3. Consultas iniciais para validação
-- =========================================================

SELECT * FROM coleta LIMIT 10;

SELECT
    marketplace,
    produto,
    marca,
    preco,
    vendas_estimadas
FROM coleta
LIMIT 20;



-- =========================================================
-- 4. Filtros rápidos (exemplos)
-- =========================================================

-- Produtos da marca Max Titanium
SELECT *
FROM coleta
WHERE marca = 'Max Titanium';

-- Produtos com avaliação alta
SELECT *
FROM coleta
WHERE avaliacao >= 4.8;



-- =========================================================
-- 5. View Geral (Base para Power BI)
-- =========================================================

CREATE OR REPLACE VIEW vw_coleta_geral AS
SELECT
    data_coleta,
    marketplace,
    produto,
    marca,
    peso_g,
    preco,
    vendas_estimadas,
    (preco * vendas_estimadas) AS receita_estimada,
    avaliacao,
    num_avaliacoes
FROM coleta;



-- =========================================================
-- 6. Views de KPIs
-- =========================================================

-- KPIs por Marca
CREATE OR REPLACE VIEW vw_kpi_marca AS
SELECT
    marca,
    ROUND(AVG(preco)::NUMERIC, 2) AS preco_medio,
    SUM(vendas_estimadas) AS total_vendas,
    ROUND(SUM(preco * vendas_estimadas)::NUMERIC, 2) AS receita_estimada,
    ROUND(AVG(avaliacao)::NUMERIC, 2) AS avaliacao_media,
    SUM(num_avaliacoes) AS total_avaliacoes
FROM coleta
GROUP BY marca;


-- KPIs por Marketplace
CREATE OR REPLACE VIEW vw_kpi_marketplace AS
SELECT
    marketplace,
    ROUND(AVG(preco)::NUMERIC, 2) AS preco_medio,
    SUM(vendas_estimadas) AS total_vendas,
    ROUND(SUM(preco * vendas_estimadas)::NUMERIC, 2) AS receita_estimada,
    ROUND(AVG(avaliacao)::NUMERIC, 2) AS avaliacao_media
FROM coleta
GROUP BY marketplace;



-- =========================================================
-- 7. Conferindo Views
-- =========================================================

SELECT * FROM vw_kpi_marca ORDER BY receita_estimada DESC;
SELECT * FROM vw_kpi_marketplace;
SELECT * FROM vw_coleta_geral LIMIT 10;



-- =========================================================
-- 8. Índices (Performance)
-- =========================================================

CREATE INDEX IF NOT EXISTS idx_coleta_data
ON coleta (data_coleta);

CREATE INDEX IF NOT EXISTS idx_coleta_marca
ON coleta (marca);

CREATE INDEX IF NOT EXISTS idx_coleta_marketplace
ON coleta (marketplace);

CREATE INDEX IF NOT EXISTS idx_coleta_produto
ON coleta (produto);

-- Índice composto (Marketplace + Produto)
CREATE INDEX IF NOT EXISTS idx_coleta_marketplace_produto
ON coleta (marketplace, produto);



-- =========================================================
-- 9. Consultas Analíticas (KPIs)
-- =========================================================

-- Receita total estimada por marca
SELECT
    marca,
    ROUND(SUM(preco * vendas_estimadas)::NUMERIC, 2) AS receita_estimada
FROM coleta
GROUP BY marca
ORDER BY receita_estimada DESC;


-- Preço médio por marketplace
SELECT
    marketplace,
    ROUND(AVG(preco)::NUMERIC, 2) AS preco_medio
FROM coleta
GROUP BY marketplace
ORDER BY preco_medio DESC;


-- Top 5 produtos mais vendidos
SELECT
    produto,
    marca,
    SUM(vendas_estimadas) AS total_vendas
FROM coleta
GROUP BY produto, marca
ORDER BY total_vendas DESC
LIMIT 5;


-- Melhor custo-benefício (alta avaliação + menor preço)
SELECT
    produto,
    marca,
    ROUND(AVG(preco)::NUMERIC, 2) AS preco_medio,
    ROUND(AVG(avaliacao)::NUMERIC, 2) AS avaliacao_media
FROM coleta
GROUP BY produto, marca
HAVING AVG(avaliacao) >= 4.7
ORDER BY preco_medio ASC;


-- Receita por marketplace ao longo do tempo
SELECT
    data_coleta,
    marketplace,
    ROUND(SUM(preco * vendas_estimadas)::NUMERIC, 2) AS receita_estimada
FROM coleta
GROUP BY data_coleta, marketplace
ORDER BY data_coleta, marketplace;



-- =========================================================
-- 10. Performance Check (EXPLAIN)
-- =========================================================

EXPLAIN ANALYZE
SELECT *
FROM coleta
WHERE marca = 'Max Titanium';