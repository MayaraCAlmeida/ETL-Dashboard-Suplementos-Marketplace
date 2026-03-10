### KPIs principais
Receita Total = SUM(vw_coleta_geral[receita_estimada])

Total Vendas = SUM(vw_coleta_geral[vendas_estimadas])

Preço Médio = AVERAGE(vw_coleta_geral[preco])


### Metas e Projeções
Meta Venda Total = [Total Vendas] * 1.10

Diferença vs Meta = [Meta Venda Total] - [Total Vendas]

Preço Médio - Meta (-2%) = [Preço Médio] * 0.98

### Receita Projetada (+5%)
Receita Projetada = [Receita Total] * 1.05

Diferença Receita vs Meta =
[Receita Projetada] - [Receita Total]

### Qualidade e Avaliações (Média Ponderada)
Avaliação Média =
DIVIDE(
    SUMX(
        vw_coleta_geral,
        vw_coleta_geral[avaliacao] * vw_coleta_geral[num_avaliacoes]
    ),
    SUM(vw_coleta_geral[num_avaliacoes])
)