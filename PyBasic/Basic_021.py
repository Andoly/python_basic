estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k,v in e.items():
        print(v," ", end = ' ')
    print()
