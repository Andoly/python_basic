import random
color = {'clean' : '\033[m',
         'blue' : '\33[34m',
         'yellow' : '\33[33m',
         'black_white' : '\33[7;30m'
         }

cont=1
comp = random.randint(1,5)
user = int(input('{}Escolha um número :'.format(color['blue'])))

while comp!=user:
    user = int(input('Digite um número : '))
    #print('User won' if comp == user else 'Machine won {}'.format(color['blue']))
    cont+=1
print('Usuário acertou depois de {} tentativas'.format(cont))
print('Número sorteado : {}'.format(comp))

print('=-'*60)

lista = []
for n in range(5):
    aux = random.randint(1,100)
    lista.append(aux)
    print("{}º número : {}".format(n+1,aux))
print("Menor : {}".format(min(lista)))
print("Maior : {}".format(max(lista)))

print('=-'*60)

lados = []
for n in range(3):
    aux = random.randint(2,10)
    lados.append(aux)
    print("{}º lado = {}".format(n+1,aux))
if((lados[0] + lados[1]> lados[2]) and (lados[1] + lados[2] > lados[0]) and (lados[0] + lados[2] > lados[1])):
    print('Os lados sorteados formam um triangulo')
else:
    print("Os lados sorteados não formam um triangulo")


