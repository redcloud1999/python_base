#!/usr/bin/env python3

"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""

__version__ = '0.1.0'
__author__ = 'Otávio'
__license__ = 'unlicense'

import sys

valid_operations = ['sum', 'div', 'sub', 'mul']
arguments = sys.argv[1:]

if len(arguments) != 3:
    arguments.append('Insira a operação: ')
    arguments.append('Insira o primeiro número: ')
    arguments.append('Insira o segundo número: ')

elif arguments[0] not in valid_operations:
    print(f'Invalid operation {sys.argv[1]} insert(sum, mul, div, sub)')
    sys.exit(0)
else:
    operation, *nums = arguments

nums[0] = float(nums[0])
nums[1] = float(nums[1])

op = 0

if operation == 'sum':
    op = int(nums[0]) + int(nums[1])
elif operation == 'div':
    op = int(nums[0]) + int(nums[1])
elif operation == 'sub':
    op = int(nums[0]) + int(nums[1])
elif operation == 'mul':
    op = int(nums[0]) + int(nums[1])

print(op)

