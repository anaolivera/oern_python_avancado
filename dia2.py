# -*- coding: utf-8 -*-
#%% FUNCAO INPUT
s = input()
s

name= input('Qual o seu nome? ')
name

x= input('Introduza o seu nome: ')
print('Olá, ', x)

n= input('Introduza um número: ')
print(n + 100) #dá erro porque tenta adicionar um inteiro a uma string

n=int(input('Introduza um número: '))
print(n + 100)

#%%FUNCAO INPUT COM EVALUATION

x= input('Introduza um número: ')
print(x)
print(type(x))

y= eval(input('Introduza um número: '))
print(y)
print(type(y))

#%%FUNCAO OUTPUT - PRINT()
print()
print("Olá Planeta Terra")
print("Qual é a sua resposta?", 42)

"Uso de aspas duplas"

'Uso de aspas simples'

"""Uso aspas triplas
para multiplas
linhas"""

print('Uso aspas triplas\npara multiplas\nlinhas')

#%% SEQUENCIAS DE ESCAPE
print("Primeira linha \nSegunda linha\n\tTerceira linha com tab")
print("Inserir aspas em strings \" or\' ")
print("No caso de querer backslash? \\ ")

#%% FORMATACAO DE STRINGS

first = "David"
last="Bowie"
age=69

message = "Olá " + "Mundo!"
message = 'O meu nome é {1}, {0} {1}'.format('David', 'Bowie')
message = f'Tenho {age} anos de idade.'

message='Caso Sr. %s, seja bem vindo' % last

print(message)
print('O meu nome é %s, ou melhor, %s %s' %(last, first,last))

print('O David Bowie faleceu com %d anos de idade' % age)

import math
print('pi: %f \nshort pi %0.2f' %(math.pi,math.pi))

message =f'Caro sr. {last}, seja bem vindo.'
print(message)

print(f'O nome é {last}, {first} {last}.')
print(f"A idade de Bowie a multiplicar por pi é {age*math.pi}")
print(f"A idade de Bowie a multiplicar por pi é {age*math.pi:.2f}")

#%% SEPARACAO DE CARACTERES

print('Existem', 6, 'membros dos Monty Python')

message = 'Existem' + 6 + 'membros dos Monty Python'
# nao concatena porque temos mistura de string com int
message = 'Existem' + str(6) + 'membros dos Monty Python'

print(message)

# não assume os espaços

print('Existem', 6, 'membros dos Monty Python', sep=' ')
print('Existem', 6, 'membros dos Monty Python', sep=None)
print('Existem', 6, 'membros dos Monty Python', sep='\n')




