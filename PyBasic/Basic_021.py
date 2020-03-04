
resultado = dict()
princ = list()
while True:
    resultado['Nome'] = str(input('Nome do aluno: '))
    resultado['Media'] = float(input(f'Média obtida por {resultado["Nome"]}:'))

    if resultado['Media'] >= 7:
        resultado['Situação'] = 'Aprovado'
    else:
        resultado['Situação'] = 'Reprovado'

    princ.append(resultado.copy())

    while True:
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
        if answer in 'SN':
            break
    if answer == 'N':
        break
print(resultado)
for resultado in princ:
    for k,v in resultado.items():
        print(f'{k} : {v} | ',end = ' ')
    print()




