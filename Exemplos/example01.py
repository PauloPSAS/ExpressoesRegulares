# Procurando vários endereços de emails em um texto
import re

text = 'purple alice@google.com, blah monkey bob_@abc.com blah dishwasher'
emails = re.findall(r'[\w.-]+@[\w.-]+', text)
if emails:
    for email in emails:
        print('Endereço: ', email)
else:
    print('not found.')
