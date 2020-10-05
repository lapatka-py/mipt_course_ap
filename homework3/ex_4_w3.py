import json

with open('1.json', 'r+') as file:
    A = file.read()
    print(A)
    B = json.loads(A)
    print(B)
    B['glossary']['GlossDiv']['GlossList']['GlossEntry']['week'] = '3'
    file.
