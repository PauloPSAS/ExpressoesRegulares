# Separando o nome de usuário e o dominio em uma busca por um email em um texto
import re

text = 'Blah monkey bob_@abc.com blah dishwasher'

match = re.search(r'([\w.-]+)@([\w.-]+)', text)

if match:
    print('email: ', match.group())
    print('usuário: ', match.group(1))
    print('dominio: ', match.group(2))
else:
    print('Not found')

