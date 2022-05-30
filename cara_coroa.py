from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())