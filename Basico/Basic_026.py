from time import sleep
from random import randint

numeros = list()
def sorteio(number, num):
    for i in range(0,num):
        num = randint(1,10)
        numeros.append(num)
        sleep(0.3)
        print(f'{num}', end=' ')
        sleep(0.3)

def somaPar(number):
    soma = 0
    for i in number:
        if i % 2 == 0:
            soma +=i
    print(f'\nA soma dos valores pares é {soma}')

def CallSorted():
    Xnumb = int(input('Quantidade de números pro vetor : '))
    sorteio(numeros, Xnumb)
    somaPar(numeros)


def escreva(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo ==0:
        passo = 1

    print(f'\nContagem de {inicio} a {fim} de {passo} em {passo} ')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont +=passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont -=passo

def maior(*num):
    bigger = count = 0
    print(f'\n{num}')
    for valor in num:
        if count==0:
            bigger = valor
        elif valor > bigger:
            bigger = valor
        count +=1
    print(f'Foram informados {count} valores e o maior é {bigger}')

def texto():
    caracteres = str(input('\nDigite uma frase ou texto: '))
    escreva(caracteres)

def contagem():
    contador(1, 10, 1)
    contador(10, 0, 2)
    print('\nUsuário decide a forma da contagem')
    i = int(input('Valor inicial da contagem : '))
    f = int(input('Valor final da contagem : '))
    p = int(input('Intervalo da contagem : '))
    contador(i,f,p)

contagem()
texto()
maior(3,2,1,6,7,9)
maior(3,15,1,19,16,17,13,6)
CallSorted()
