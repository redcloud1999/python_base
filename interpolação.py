#!/usr/bin/env python3

import os
import sys
import smtplib
from email.mime.text import MIMEText


arguments = sys.argv[1:]
if not arguments:
    print('informe o nome do arquivo de emails')
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

with smtplib.SMTP(host='localhost', port=8025) as server:



    for line in open(filepath):
        name, email = line.split(',')
        text = (
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

        from_ = 'trindade_otavio@hotmail.com'
        to = ', '.join([email])
        message = MIMEText(text, 'html')
        message['Subject'] = 'Compre mais'
        message['from'] = from_
        message['To'] = to

        server.sendmail(from_, to, message.as_string())

        
