"""Exemplo funções"""


"""
f(x) = 5 * (x / 2)



"""

# tudo ensinado até aqui eu manjo mais ou menos



def double(x):
    return x * 2

print(double(67))

############

def print_in_upper(string):
    """Procedure with no explict return"""
    print(string.upper())
    # implicit return none

print_in_upper('mundo python')

#######################

from math import sqrt

def heron(a, b, c):
    """Calcula a area de um triangulo"""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5 # que é = math.sqrt(area)

triangulos = [
    (3, 4, 5), 
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
]


for t in triangulos:
    area = heron(*t)
    print(f'A Area do triangulo é: {area} ')

def nome_da_funcao():
    print('Hello função')
    return 1

nome_da_funca0()































