
email_tmpl = '''

Olá, %(nome)s
 
Tem interesse em comprar %(produto)s
 
Este produto é otimo para resolver
%(texto)s
 
CLique agora em %(link)s
 
Apenas %(quantidade)d disponiveis!
 
Preço promocional %(preco).2f
'''

clientes = ['Maria', 'João', 'Bruno']

for cliente in clientes:
    print(
        email_tmpl 
        % {
            'nome': cliente, 
            'produto': 'Caneta',
            'texto': 'Escreve muito bem',
            'link': 'https://canetaslegais.com',
            'quantidade': 1,
            'preco': 50.5
        }
        )
