from extras.addons import IMC, IMCI
import argparse
import sqlite3
import pandas as pd
import datetime

#%% inicializar parser
parser = argparse.ArgumentParser(prog='IMC',		
								 description='calculadora do indice de massa corporal')

parser.add_argument('-pn', dest='pnome', action='store', type=str, required=True,
                    nargs='?', help='primeiro nome')

parser.add_argument('-un', dest='unome', action='store', type=str, required=True,
                    nargs='?', help='ultimo nome')

parser.add_argument('-al', dest='altura', action='store', type=float, required=True,
                    nargs='?', help='altura (m)')

parser.add_argument('-pe', dest='peso', action='store', type=int, required=True,
                    nargs='?', help='peso (kg)')

args = parser.parse_args()


#%% verificacao dos valores
if not args.pnome.isalpha(): parser.error('PNOME invalido')
if not args.unome.isalpha(): parser.error('UNOME invalido')

if args.altura <= 0: parser.error('ALTURA > 0 m')
if args.peso <= 0 or args.peso >= 200: parser.error('0 kg < PESO < 200 kg')


#%% conversao de valores para o programa
pnome  = args.pnome.lower()
unome  = args.unome.lower()
altura = args.altura
peso   = args.peso


#%% funcoes IMC e IMCI
imc  = IMC(altura, peso)
imci = IMCI(altura, peso)

#%% resultado formatado
print('IMC: %.2f \nIMCI: %.2f \nEstado: ' %(imc, imci), end='')


#%% classificacao de resultados
if imc <= 18.5:             print('MAGRO')
elif 18.5 <= imc <= 24.9:   print('NORMAL')
elif 25 <= imc <= 29.9:     print('FORTE')
elif imc >= 30:             print('OBESO')


#%% inicializar sqlite
time = datetime.datetime.now()

conn = sqlite3.connect('imcdata.db')
curs = conn.cursor()

# criar tabela sqlite
curs.execute('''CREATE TABLE IF NOT EXISTS users
             (pnome text, unome text, altura real, peso int, imc real, imci real, timestamp text)''')

curs.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?)', 
             (pnome, unome, altura, peso, imc, imci, str(time)))

# exportar tabela sqlite para ficheiro texto
dbdf = pd.read_sql('SELECT * FROM users', conn)
dbdf.to_csv('users.csv', index=False)

# fechar sqlite
conn.commit()
curs.close
conn.close()
