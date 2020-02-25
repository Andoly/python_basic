# Ordenando em tempo real, sem usar o método sorted()

lista5 = list()

for i in range(0,5):
    valor = int(input(f'Digite {i+1}º item : '))
    if i == 0 or valor > lista5[-1]:
        lista5.append(valor)
    else:
        pos = 0
        while pos < len(lista5):
            if valor <= lista5[pos]:
                lista5.insert(pos, valor)
                break
            pos +=1
print(f'Exibindo a lista ordenada : {lista5}')

