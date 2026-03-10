"""
utils.py

Módulo com funções auxiliares para tratamento e padronização
de dados coletados em marketplaces (preços, avaliações, vendas etc.).

"""

import re
from typing import Optional


def limpar_preco(preco_texto: str) -> Optional[float]:
    """
    Converte preços em formato brasileiro (ex: "R$ 129,90")
    para valores numéricos do tipo float.

    Parâmetros
    ----------
    preco_texto : str
        Texto contendo o preço extraído.

    Retorno
    -------
    float ou None
        Valor numérico convertido ou None caso inválido.
    """
    if not preco_texto:
        return None

    try:
        return float(
            preco_texto.replace("R$", "").replace(".", "").replace(",", ".").strip()
        )
    except ValueError:
        return None


def extrair_numero(texto: str) -> Optional[int]:
    """
    Extrai o primeiro número inteiro encontrado em uma string.

    Exemplo:
    --------
    "4.200 avaliações" → 4200

    Parâmetros
    ----------
    texto : str
        Texto contendo números misturados.

    Retorno
    -------
    int ou None
        Primeiro número encontrado ou None caso não exista.
    """
    if not texto:
        return None

    numeros = re.findall(r"\d+", texto.replace(".", ""))

    return int(numeros[0]) if numeros else None
