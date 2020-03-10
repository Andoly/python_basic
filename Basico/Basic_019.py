from random import randint
from time import sleep
mega = list()
list_mega = list()
amount = int(input('Quantas sugestões de jogos : '))
total = 1
while total <= amount:
    cont = 0
    while True:
        digit = randint(1,60)
        if digit not in mega:
            mega.append(digit)
            cont += 1
        if cont >= 6:
            break
    mega.sort()
    list_mega.append(mega[:])
    mega.clear()
    total +=1
print('-=',f'Sorteando {amount} jogos da mega sena')

for i,jogo in enumerate(list_mega):
    print(f'Jogo {i+1} : {jogo}')
    sleep(2)


