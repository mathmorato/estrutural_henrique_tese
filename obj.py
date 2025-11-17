# ============================================================
# 1. Definição da função estado-limite
# ============================================================

def of_conf(x, args=None): 
    """
    Função estado-limite: g = z * fy - m
    x[0] = z (módulo resistente plástico)
    x[1] = fy (tensão de escoamento do aço)
    x[2] = M_d (momento solicitante)
    """
    g = x[0] * x[1] - x[2]
    return [g]