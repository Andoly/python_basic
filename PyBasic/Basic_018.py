from random import randint
# Exemplo 1

composta = [[] , []]
matriz = [[0,0,0], [0,0,0], [0,0,0]]
valor = 0

for i in range(0,7):
    while True:
        try:
            valor = int(input(f'Digite o {i+1}º valor : '))
            if valor % 2 == 0:
                composta[0].append(valor)
            else:
                composta[1].append(valor)
            break

        except ValueError:
            print('Valor incorreto. Digite novamente')
composta[0].sort()
composta[1].sort()

print(f'Lista com números pares em ordem crescente : {composta[0]}')
print(f'Lista com números impares em ordem crescente : {composta[1]}')

# Exemplo 2
maior = column3 = soma = aux = 0

for row in range(0,3):
    for column in range(0,3):
        # matriz[row][column] = int(input(f'Valor para linha {row+1} coluna {column+1} :'))
        matriz[row][column] = randint(1,9)
        if matriz[row][column] % 2 == 0:
            soma +=matriz[row][column]

        if column == 2:
            column3 += matriz[row][column]

        if row == 1:
            if matriz[row][column] > maior:
                maior = matriz[row][column]

for row in range(0,3):
    for column in range(0,3):
        print(f'[{matriz[row][column]:^3}]', end = '')
    print()

print(f'Soma de todos os valores pares : {soma}')

# A soma dos valores da terceira coluna
print(f'Soma de todos valores terceira coluna : {column3}')

# O maior valor da segunda linha
print(f'Maior valor da linha 2 : {maior}')

