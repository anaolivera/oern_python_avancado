# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:50:33 2020

@author: anacv
"""
#%%Primeira abordagem
#recolher informacao de input e formatar output

altura = float(input('Introduza a sua altura em metros (m):'))
peso = float(input('Introduza o seu peso em quilogramas (kg):'))

print('I índice de massa corporal (IMC) é: ',round(peso/(altura*altura),2))

#%% segunda abodagem

altura = float(input('Introduza a sua altura em metros (m):'))
peso = float(input('Introduza o seu peso em quilogramas (kg):'))

imc=peso/(altura**2)

print('O seu IMC é {0} e o seu estado é: '.format(round(imc,2)), end='') #com end=None ele muda de linha

#condicoes
if (imc<16):
    print('muito abaixo do peso ideal')
elif (imc >= 16 and imc<18.5):
    print('abaixo do peso ideal')
elif (imc >=18.5 and imc <25):
    print('saudável')
elif(imc >=25 and imc <30):
    print('acima do peso ideal')
elif(imc >= 30):
    print('muito acima do peso ideal')

#%% terceira abordagem
print('CALCULADORA DO ÍNDICE DE MASSA CORPORAL\n')

def IMC(altura,peso):
    imc=peso/(altura**2)
    return imc

#Gestao de erros

while True:
    try:
        altura=float(input('Introduza a sua altura em metros (m):'))
        break
    except ValueError:
        print('Introduza um valor numérico válido para a altura: ')

if altura <0:
    print('A altura não pode ser inferior a 0')
        
while True:
  try:
      peso=float(input('Introduza o seu peso em quilogramas (kg):'))
      break
  except ValueError:
      print('Introduza um valor numérico válido para o peso: ')  

if peso <0 or peso > 500:
    print('O seu peso não poderá ser menor que 0 kg e maior que 500 kg')

#chamar a funcao IMC
imc=IMC(altura,peso)

print('\n O seu Índice de Massa Corporal é %.2f\n' %imc) 

#Verificacao do estado de peso do  utilizador

if (imc<16):
    print('muito abaixo do peso ideal')
elif (imc >= 16 and imc<18.5):
    print('abaixo do peso ideal')
elif (imc >=18.5 and imc <25):
    print('saudável')
elif(imc >=25 and imc <30):
    print('acima do peso ideal')
elif(imc >= 30):
    print('muito acima do peso ideal') 
else:
    print('Certifique-se que introduziu valores corretos')


#%% quarta abordagem

print('CALCULADORA DO ÍNDICE DE MASSA CORPORAL\n')

altura = float(input('Introduza a sua altura em metros (m):'))
peso = float(input('Introduza o seu peso em quilogramas (kg):'))


def IMC(altura,peso):
    imc=peso/(altura**2)
    return imc

#Gestao de valores anormais de peso e altura
if altura<0:
    print('Não pode ter altura negativa.')
    raise Exception('exit') # apenas para o programa. podia-se usar exit() mas isso reiniciava o kernel

if altura<1:
    print('Com altura de '+str(altura)+' metros deve ser uma criança. Esta calculadora é só para adultos!')
    raise Exception('exit')

if altura>3:
    print('Tem a certeza que introduziu de valor correto de '+ str (altura)+' metro de altura?')
    raise Exception('exit')

if altura>4:
    print('A sua altura não pode exceder os 3 metros.')
    raise Exception('exit')

if peso<0:
    print('O seu peso não pode ser negativo.')

if peso<40:
    print('Com peso de '+str(peso)+ ' kg, deve ser uma criança.')
    raise Exception('exit')
if peso >200:
    print('Tem a certeza que introduziu de valor correto de '+ str (peso)+' quilogramas?')
        
        
 #chamar a funcao IMC
imc=IMC(altura,peso)

print('\n O seu Índice de Massa Corporal é %.2f\n' %imc) 

#Verificacao do estado de peso do  utilizador

if (imc<16):
    print('muito abaixo do peso ideal')
elif (imc >= 16 and imc<18.5):
    print('abaixo do peso ideal')
elif (imc >=18.5 and imc <25):
    print('saudável')
elif(imc >=25 and imc <30):
    print('acima do peso ideal')
elif(imc >= 30):
    print('muito acima do peso ideal') 
else:
    print('Certifique-se que introduziu valores corretos')
       
#%%quinta abordagem

from extras.addons import IMC
import extras.addons as ex

print('CALCULADORA DO ÍNDICE DE MASSA CORPORAL\n')

altura = float(input('Introduza a sua altura em metros (m):'))
peso = float(input('Introduza o seu peso em quilogramas (kg):'))


#Gestao de valores anormais de peso e altura
if altura<0:
    print('Não pode ter altura negativa.')
    raise Exception('exit') # apenas para o programa. podia-se usar exit() mas isso reiniciava o kernel

if altura<1:
    print('Com altura de '+str(altura)+' metros deve ser uma criança. Esta calculadora é só para adultos!')
    raise Exception('exit')

if altura>3:
    print('Tem a certeza que introduziu de valor correto de '+ str (altura)+' metro de altura?')
    raise Exception('exit')

if altura>4:
    print('A sua altura não pode exceder os 3 metros.')
    raise Exception('exit')

if peso<0:
    print('O seu peso não pode ser negativo.')

if peso<40:
    print('Com peso de '+str(peso)+ ' kg, deve ser uma criança.')
    raise Exception('exit')
if peso >200:
    print('Tem a certeza que introduziu de valor correto de '+ str (peso)+' quilogramas?')
        
        
 #chamar a funcao IMC
imc=ex.IMC(altura,peso)

print('\n O seu Índice de Massa Corporal é %.2f\n' %imc) 

#Verificacao do estado de peso do  utilizador

if (imc<16):
    print('muito abaixo do peso ideal')
elif (imc >= 16 and imc<18.5):
    print('abaixo do peso ideal')
elif (imc >=18.5 and imc <25):
    print('saudável')
elif(imc >=25 and imc <30):
    print('acima do peso ideal')
elif(imc >= 30):
    print('muito acima do peso ideal') 
else:
    print('Certifique-se que introduziu valores corretos')
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        