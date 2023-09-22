# Combinando findall() com groups retornará uma lista de tuplas
import re

texto = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

tuples = re.findall(r'([\w\\.-]+)@([\w\\.-]+)', texto)
for tupla in tuples:
    print()
    print('username: ', tupla[0])
    print('host: ', tupla[1])
