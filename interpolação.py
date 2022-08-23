import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print('informe o nome do arquivo de emails')
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


for line in open(filepath):
    name, email = line.split(',')

    # TODO: substituir por envio de email
    print(f'Enviando email para {email}')
    print(
        open(templatepath).read() 
        % {
            'nome': name, 
            'produto': 'Caneta',
            'texto': 'Escreve muito bem',
            'link': 'https://canetaslegais.com',
            'quantidade': 1,
            'preco': 50.5
        }
        )
    print("-" * 50)
