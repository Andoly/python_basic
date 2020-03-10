from random import randint
cont = 0

while True:
    choice = str(input('IMPAR [I] ou PAR [P] ?')).strip()
    while choice not in 'IiPp':
        choice = str(input('IMPAR [I] ou PAR [P] ?'))

    player= int(input('Escolha um número : '))
    while player is not enumerate and 0 <= player > 9:
        player = int(input('Escolha um número : '))

    machine = randint(0, 10)
    print('Número escolhido pelo a maquina : {}'.format(machine))

    game = player + machine

    if game % 2 == 0 and choice in 'Pp':
        cont +=1
        print('Voce venceu\n')

    elif game % 2 == 1 and choice in 'Ii':
        cont +=1
        print('Voce venceu\n')

    else :
        print('Game Over\n')
        break

print('Jogador venceu {} consecutiva(s)'.format(cont))


















