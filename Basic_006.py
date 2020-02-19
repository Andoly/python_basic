
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
number = int(input('Número para conversão : '))
conv = 0
while (conv >3 or conv <1):
    conv = int(input('[ 1 ] Inteiro para binário \n[ 2 ] Inteiro para octal\n[ 3 ] Inteiro para hexadecimal\nOpção : '))
    if(conv == 1):
         print('Binário de {} = {}'.format(number,bin(number)[2:]))
    elif(conv == 2):
         print('Octal de {} = {}'.format(number,oct(number)[2:]))
    elif(conv == 3):
        print('Hexadecimal de {} = {}'.format(number,hex(number)[2:]))
    else:
         print('Opção invalida')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
num = []
soma = 0
cont = 0
for n in range(0,500,3):
    if n%2 != 0:
        num.append(n)
        soma +=n
        cont +=1
print("{}".format(num))
print('Soma de multiplos de 3 no intervalo de 1 a 500 : {}'.format(soma))
print('Quantidade de números : {}'.format(cont))

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
frase = str(input('Digite uma frase : ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]

print(junto, inverso)


