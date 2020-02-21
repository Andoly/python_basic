withdraw = float(input('Valor a ser sacado : '))
total = withdraw
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break

total_spend = product1000 = menor = cont = 0
product_cheap = ' '

while True:
    name_product = str(input('Nome do produto : ')).strip()
    try:
        price = float(input(f'Preço {name_product} : '))
        if type(price) != float:
            print('Valor invalido')
    except ValueError as e:
        price = float(input(f'Preço {name_product} : '))
    cont +=1

    total_spend += price
    if price > 1000:
        product1000 += 1

    if cont == 1 or price < menor:
        menor = price
        product_cheap = name_product

    register = ' '
    while register not in 'SN':
        register = str(input('Deseja adquirir um novo produto? [S / N] ')).strip().upper()[0]
    if register == 'N':
        break
print(f'Saque de {withdraw} realizado com sucesso')
print(f'\nO total da compra foi de R${total_spend}')
print(f'Restou R$ {withdraw - total_spend}')
print(f'{product1000} custaram mais de R$ 1000')
print(f'O produto mais barato foi {product_cheap} custando R$ {menor}')

