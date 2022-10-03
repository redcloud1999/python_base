#!/usr/bin/env python3

# definição ou atribuição
# assinatura
# documentação / docstring
# codigo
# valor de retorno

# - parametro
# posicional - passados em ordem


def nome_da_funcao(a, b, c):
    """Esta função faz algo com a, b e c.

    Use esta função quando quiser a + b + c
    quando o parametro a tiver o valor 10
    vai acontecer x.

    >>>nome_da_funcao(1, 2, 3)
    6
    """
    resultado = a + b + c
    return resultado

# passagem de argumentos posicionais
valor = nome_da_funcao(1, 2, 3)

# passagem de argumentos nomeados
valor = nome_da_funcao(a=1, b=2, c=3)

# passagem de argumentos mista
# argumentos posicionais antes dos nomeados
valor = nome_da_funcao(1, 2, c=3)
valor = nome_da_funcao(
    a=1,
    c=2,
    b=3,
)



print(valor)

###################################################

def outra_funcao(a, b, c):
    """Explica oque ela faz"""

    # tupla como valor de retorno
    return a * 2, b * 2, c * 2
    
valor1, valor2, valor3 = outra_funcao(2, 3, 4)

valor1, *_ = outra_funcao(2, 3, 4)

###################################################



# passagem de argumentos com desempacotamento

def soma(n1, n2):
    """faz a soma de 2 números"""
    return n1 + n2


# normal
print(soma(10, 20))

# argumentos em sequencia
args = (10, 20)   # tuple
print(soma(args[0], args[1]))
print(soma(*args))

# argumentos dicionario / nomeados
args = {'n2': 90, 'n1': 100}
print(soma(**args))

lista_de_valores_para_somar = [
    {'n2': 90, 'n1': 100}, 
    {'n2': 90, 'n1': 200},
    {'n2': 9, 'n1': 650}
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))


###################################################









