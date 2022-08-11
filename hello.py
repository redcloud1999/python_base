#!/usr/bin/env python3

"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 Hello.py
    ou
    ./hello.py

"""

__version__ = '0.0.1'
__author__ = 'Otávio Trindade'
__license__ = 'Unlicense'

import os

current_language =  os.getenv('LANG', 'en_US')[:5]

msg = 'Hello, World!'

if current_language == 'pt_BR':
    msg = 'Olá, Mundo!'
if current_language == 'it_IT':
    msg = 'Ciao, Mondo!'
if current_language == 'es_SP':
    msg = 'Hola, Mundo!'
if current_language == 'fr_FR':
    msg = 'Bonjour, Monde!'
                

print(msg)
