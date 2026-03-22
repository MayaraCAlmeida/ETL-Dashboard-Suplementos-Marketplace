import re
from typing import Optional


def limpar_preco(preco_texto: str) -> Optional[float]:
    if not preco_texto:
        return None
    try:
        return float(
            preco_texto.replace("R$", "").replace(".", "").replace(",", ".").strip()
        )
    except ValueError:
        return None


def extrair_numero(texto: str) -> Optional[int]:
    # ex: "4.200 avaliações" → 4200
    if not texto:
        return None
    numeros = re.findall(r"\d+", texto.replace(".", ""))
    return int(numeros[0]) if numeros else None
