aluno = list()
escola = list()
while True:
    aluno.append(str(input('Nome do aluno : ')).strip())
    aluno.append(float(input('Nota 1 : ')))
    aluno.append(float(input('Nota 2 : ')))

    Mid = (aluno[1]+aluno[2])/2
    aluno.append(Mid)

    escola.append(aluno[:])
    aluno.clear()

    while True:
        answer = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
        if answer in 'SN':
            break
    if answer == 'N':
        break

print(f'\n{"ID":<4}{"Aluno":<10}{"Média":>8}')

for pos, valor in enumerate(escola):
    print(f'{pos:<4}{valor[0]:<10}{valor[3]:>6.1f}')

while True:
    option = int(input('Digite o ID do aluno que deseja visualização ou 999 - Finalizar: '))
    if option == 999:
        break
    if option < len(escola):
        print(f'\n{escola[option][0]} obteve N1 = {escola[option][1]} e N2 = {escola[option][2]}\n')
