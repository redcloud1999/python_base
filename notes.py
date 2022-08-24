#!/usr/bin/env python3

"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre carreira em tecnologia

$$ notes.py read --tag=tech
"""
__version__ = '0.1.0'
__author__ = 'Otávio'

import os
import sys


cmds = ('read', 'new')
path = os.curdir
filepath = os.path.join (path, 'notes.txt')

arguments = sys.argv[1:]

if not arguments:
    print('Invalid usage')
    print('You must specify subcommand {}'.format(cmds))
    sys.exit(1)


if arguments[0] not in cmds:
    print(f'Invalid command {arguments[0]}')
    sys.exit(1)

if arguments[0] == 'read':
    for line in open(filepath):
        title, tag, text  = line.split('\t')
        if tag == arguments[1].lower():
            print(f'Title: {title} ')
            print(f'text: {text}')
            print('*' * 40)
            print()
            
elif arguments[0] == 'new':
    title = arguments[1] # TODO:  tratar exception
    text = [
        f'{title}',
        input('tag: ').strip(),
        input('text:\n' ),
    ]
    #\t - tsv
    with open(filepath, 'a') as file_:
        file_.write('\t'.join(text) + '\n')
