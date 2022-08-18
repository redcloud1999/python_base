#!/usr/bin/env python3

"""Exibe relatório de crianças por atividade.

Imprimir a lista de crinças agrupadas por sala
que frequenta cada uma das atividades.
"""

sala1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala2 = ['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda']

aula_ingles = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
aula_musica = ['Erik', 'Carlos', 'Maria']
aula_danca = ['Gustavo', 'Sofia', 'Joana', 'Antonio']



# Listar alunos em cada atividade por sala

atividades = [
        ('Ingles', aula_ingles), 
        ('Música', aula_musica),
        ('Dança',  aula_danca),
        ]

for nome_atividade, atividade in atividades:

    print('{:^50}'.format(f'Alunos da atividade {nome_atividade}\n'))
    atividade_sala1 = []
    atividade_sala2 = []
    

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
           atividade_sala2.append(aluno)


    print('         {:<50}'.format(f'sala 1: {atividade_sala1}'))
    print('         {:<50}'.format(f'sala 2: {atividade_sala2}'))
    print('_' * 50)
    print()








