"""Usando o método 'sub' para alterar os nomes """

import re

frase = 'A agente Alice disse à agente Carol que a agente Eve sabia que o agente Bob era um agente duplo.'

nomesRegex = re.compile(r'agente (\w)(\w*)')

fraseNova = nomesRegex.sub(r'\1****', frase)

print('Frase sem a Regex substituida:...')
print(frase)
print()
print("Frase com a Regex de substituição:...")
print(fraseNova)
print()
