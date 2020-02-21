year18 = mentotal = woman20 = 0

while True:
    try:
        age = int(input('Digite a idade : '))
        if age < 0 and type(age) != int:
            age = int(input('Digite a idade : '))
    except ValueError as e:
        print('Idade invalida')
        age = int(input('Digite a idade : '))

    sex = ' '
    while sex not in 'MF':
        sex = str(input('Digite o sexo : [M / F]')).strip().upper()[0]
    if age > 18:
        year18 += 1
    if sex == 'M':
        mentotal += 1
    if sex == 'F' and age < 20:
        woman20 += 1

    register = ' '
    while register not in 'SN':
        register = str(input('Deseja cadastrar uma nova pessoa? [S / N] ')).strip().upper()[0]
    if register == 'N':
        break
print(f'\nTotal de pessoas com mais de 18 anos : {year18}')
print(f'Total de homens cadastrados : {mentotal}')
print(f'Total de mulher com menos de 20 anos : {woman20}')
print('Cadastros finalizado')
