somaIdade = 0
IdadeMaior = 0
nomeVelho = ''
Mulher20menos = 0
print('=-'*60)
for n in range(1,3):
    Nome = str(input('Nome {}ª pessoa: '.format(n))).strip()
    Idade = int(input('Idade {}ª pessoa: '.format(n)))
    Sexo = str(input('Sexo {}ª pessoa: [M/F]'.format(n))).strip()
    while Sexo not in 'MmFf':
        Sexo = str(input('Sexo {}ª pessoa: [M/F]'.format(n))).strip()
    somaIdade += Idade
    if n == 1 and Sexo in 'Mm':
        IdadeMaior = Idade
        nomeVelho = Nome
    if Sexo in 'Mm' and Idade > IdadeMaior:
        IdadeMaior = Idade
        nomeVelho = Nome
    if Sexo in 'Ff' and Idade < 20:
        Mulher20menos +=1

mediaIdade = somaIdade /n
print('Média de idade do grupo é de {:.2f} anos'.format(mediaIdade))
if (nomeVelho):
    print('O homem mais velho é {} com {} anos'.format(nomeVelho, IdadeMaior))
else:
    print('O grupo não contém homens')
print('Grupo contém {} menina(s) com menos de 20 anos'.format(Mulher20menos))

print('=-'*60)

n = int(input('Digite um número para operação fatorial : '))
fat = 1
i = 2
while i <= n:
    fat = fat * i
    i +=1
print('{}! = {}'.format(n,fat))

print('\nFIBONACCI '+'=-'*55)
fibo = []
n1 = 0
n2 = 1
n = int(input('Digite N para sequência de fibonacci : '))
print('{} -> {}'.format(n1,n2), end = '')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print('-> {}'.format(n3), end = '')
    n1 = n2
    n2 = n3
    cont+=1


