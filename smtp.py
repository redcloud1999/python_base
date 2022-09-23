#!/usr/bin/env python3

"""Exemplos de envio de e-mail"""

import smtplib

SERVER = 'localhost'
PORT = 8025

FROM = 'trindade_otavio@hotmail.com'
TO = ['ccbtata3@gmail.com', 'fiscal@lgcontabilidadejdi.com.br']
SUBJECT = 'Meu Email via Python'
TEXT = """\
Este é o meu email enviado pelo <b>Python<b>
"""

mensagem = f"""\
From: trindade_otavio@hotmail.com
To: ccbtata3@gmail.com, otrindade694@gmail.com
Subject: imposto


Mensagem do meu e-mail
"""

message = f"""\
From: {FROM}
To: {TO}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode('utf-8'))
    































































