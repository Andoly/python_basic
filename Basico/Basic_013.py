# Exemplo 1
from random import sample

tupla = tuple(sample(range(10),5))
print(f'Tupla : {tupla}')
print(f'O maior elemento da tupla é {max(tupla)}\nO menor elemento da tupla é {min(tupla)}')
print(f'{tupla.count(3)} ocorrência(s) do número 3 na tupla')

if 3 in tupla:
    pos = tupla.index(3)
    print(f'O valor 3 está na {pos}º posição do indice e {pos+1} da representação da tupla')
else:
    print(f'Não possui valor 3 na tupla')

print(f'Numeros pares :',end = ' ')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print(f'\n\n'+'-'*70+'\n')

# Exemplo 2
total = 0
print(f'{"Listando produtos":^45}')
Produtos = ('Batata Palha', 2.95, 'Chocolate Nestlé', 3.95, 'Coca-Cola 2L', 5.99 , 'Chandelle', 8.87 ,
            'Azeite de Oliva', 8.89 , 'Kit Creme Dental Colgate', 6.38 , 'Fralda Pampers', 14.87)
for prod in range(0,len(Produtos)):
    if prod % 2 == 0:
        print(f'{Produtos[prod]:.<40}', end ='')
    else:
        print(f'R$ {Produtos[prod]:>6.2f}')
        total +=Produtos[prod]
print(f'\nO total da compra foi de R$ {total}\n')

print(f'\n\n'+'-'*70+'\n')
print(f'{"Identificando vogais":^45}')

# Exemplo 3
palavras = ('Multilaser', 'Samsung', 'Pining', 'Avon', 'Intelbras', 'Corsair', 'Orient', 'Oakley')

for word in range(0,len(palavras)):
    print(f'\n{palavras[word]} temos as vogais : ',end = '')
    for letra in palavras[word]:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')





