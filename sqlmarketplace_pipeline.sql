-- tabela principal
SELECT table_name FROM information_schema.tables WHERE table_name = 'coleta';

CREATE TABLE IF NOT EXISTS coleta (
    id                SERIAL PRIMARY KEY,
    marketplace       VARCHAR(50),
    produto           VARCHAR(100),
    marca             VARCHAR(100),
    peso_g            INTEGER,
    preco             NUMERIC(10,2),
    vendas_estimadas  INTEGER,
    avaliacao         NUMERIC(2,1),
    num_avaliacoes    INTEGER,
    data_coleta       DATE
);


-- validação
SELECT * FROM coleta LIMIT 10;

SELECT marketplace, produto, marca, preco, vendas_estimadas
FROM coleta LIMIT 20;


-- filtros rápidos
SELECT * FROM coleta WHERE marca = 'Max Titanium';
SELECT * FROM coleta WHERE avaliacao >= 4.8;


-- views
CREATE OR REPLACE VIEW vw_coleta_geral AS
SELECT data_coleta, marketplace, produto, marca, peso_g, preco,
       vendas_estimadas, (preco * vendas_estimadas) AS receita_estimada,
       avaliacao, num_avaliacoes
FROM coleta;

CREATE OR REPLACE VIEW vw_kpi_marca AS
SELECT marca,
    ROUND(AVG(preco)::NUMERIC, 2)              AS preco_medio,
    SUM(vendas_estimadas)                       AS total_vendas,
    ROUND(SUM(preco * vendas_estimadas)::NUMERIC, 2) AS receita_estimada,
    ROUND(AVG(avaliacao)::NUMERIC, 2)          AS avaliacao_media,
    SUM(num_avaliacoes)                         AS total_avaliacoes
FROM coleta GROUP BY marca;

CREATE OR REPLACE VIEW vw_kpi_marketplace AS
SELECT marketplace,
    ROUND(AVG(preco)::NUMERIC, 2)              AS preco_medio,
    SUM(vendas_estimadas)                       AS total_vendas,
    ROUND(SUM(preco * vendas_estimadas)::NUMERIC, 2) AS receita_estimada,
    ROUND(AVG(avaliacao)::NUMERIC, 2)          AS avaliacao_media
FROM coleta GROUP BY marketplace;

SELECT * FROM vw_kpi_marca       ORDER BY receita_estimada DESC;
SELECT * FROM vw_kpi_marketplace;
SELECT * FROM vw_coleta_geral    LIMIT 10;


-- índices
CREATE INDEX IF NOT EXISTS idx_coleta_data               ON coleta (data_coleta);
CREATE INDEX IF NOT EXISTS idx_coleta_marca
