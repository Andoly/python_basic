from random import randint
from time import sleep
from operator import itemgetter

players = {}
for i in range(0,4):
    players[f'Jogador{i+1}'] = randint(1,6)
for k,v in players.items():
    print(f'{k} tirou {v}')
    sleep(1)
players = sorted(players.items(), key=itemgetter(1), reverse=True)

print(players)

print('-='*40)
print('== Ranking dos jogadores ==')
cont = 1
for j in range(0, len(players)):
    if j == 0:
        print(f'{cont}º  | {players[j][0]} com {players[j][1]} pontos')
    elif players[j][1] == players[j-1][1]:
        print(f'{cont}º  | {players[j][0]} com {players[j][1]} pontos')
    else:
        cont +=1
        print(f'{cont}º  | {players[j][0]} com {players[j][1]} pontos')

