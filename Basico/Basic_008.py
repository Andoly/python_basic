
cont = 0
soma = 0
listar = []
n = 0
while n !=999:
    n = int(input('Digite um número [999 - Opção de saida ]: '))
    if n == 999:
        print('Foi digitado opção de saida')
        break

    else:
        cont +=1
        soma +=n
        media = soma/cont
        listar.append(n)
print('Foi digitado {} números e a soma deles é {} e média é {:.2f}'.format(cont,soma, media))
print('O maior número é {}\nO menor número é {}'.format(max(listar),min(listar)))
