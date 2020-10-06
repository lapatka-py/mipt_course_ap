import json

with open('1.json', 'r+') as file:
    A = file.read()
    print(A)
    B = json.loads(A)
    B['glossary']['GlossDiv']['GlossList']['GlossEntry']['week'] = '3'
    print(B)
    #json.dump(B, file)
    C = json.dumps(B)
    file.writelines(C)