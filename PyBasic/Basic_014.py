# Exemplo 1
from random import randint
lista5 = []
aux = 0
for i in range(0,5):
    lista5.append(randint(1,100))
print(f' Lista : {lista5}\n Menor valor na lista é {min(lista5)} na posição {lista5.index(min(lista5))}\n '
      f'Maior valor na lista é {max(lista5)} na posição {lista5.index(max(lista5))}')

# Exemplo 2
listaNumber = list()
cont = 0
while True:
    numero = int(input('Digite um número : '))

    if numero not in listaNumber:
        listaNumber.append(numero)
        print(f'{numero} adicionado com sucesso')
        cont +=1

    else:
        print(f'{numero} já foi adicionado. Valor duplicado não será adicionado')

    cond = str(input('Deseja continuar ? [S/N]')).upper()

    if cond in 'nN':
        break

print(f'\nLista em ordem crescente : {sorted(listaNumber)}')
print(f'Lista em ordem decrescente : {sorted(listaNumber,reverse = True)}')
print(f'Foram digitados {cont} números')
if 5 in listaNumber:
    print(f'5 está contido na lista')
else:
    print(f'5 não está contido na lista')


