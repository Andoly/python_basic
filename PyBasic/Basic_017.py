cadastro = list()
cad_Composto = list()
cont = 0
maior = menor = 0
while True:
    cadastro.append(str(input('Nome: ')))

    while True:
        try:
            cadastro.append(float(input('Peso: ')))
            cont += 1

            if len(cad_Composto) == 0:
                maior = menor = cadastro[1]
            else:
                if cadastro[1] > maior:
                    maior = cadastro[1]
                if cadastro[1] < menor:
                    menor = cadastro[1]

            cad_Composto.append(cadastro[:])
            cadastro.clear()
            break
        except ValueError:
            print('Peso invalido. Digite novamente')

    resp = str(input('Deseja continuar? [S/N]')).upper()
    if resp in 'N':
        break

print(f'\nLista composta : {cad_Composto}')
print(f'O maior peso foi de {maior} Kg ')
print(f'O menor peso foi de {menor} Kg')
print(f'Foram cadastradas {cont} pessoas')

