total_spend = product1000 = menor = cont = 0
product_cheap = ' '
while True:
    list_product = []
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
print(f'\nO total da compra foi de R${total_spend}')
print(f'{product1000} custaram mais de R$ 1000')
print(f'O produto mais barato foi {product_cheap} custando R$ {menor}')



