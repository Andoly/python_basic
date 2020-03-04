Cadastro = {}
Lista_Cadastro = list()
Med_idade = 0
while True:

    Cadastro['Nome'] = str(input('Nome: '))
    Cadastro['Sexo'] = str(input('Sexo: [M/F]:')).strip().upper()[0]
    Cadastro['Idade'] = int(input('Idade: '))
    Med_idade += Cadastro["Idade"]
    Lista_Cadastro.append(Cadastro.copy())
    answer = str(input('Continuar ? [S/N]: ')).strip().upper()[0]
    if answer == 'N':
        break

print(Lista_Cadastro)
print(f'\nForam cadastradas {len(Lista_Cadastro)} pessoas')
print(f'\nMédia de idade = {Med_idade/len(Lista_Cadastro)}')

print(f'\nMulheres cadastradas :',end= ' ')
for i in Lista_Cadastro:
    if i['Sexo'] in 'F':
        print(f'{i["Nome"]}'',', end= ' ')

print(f'\nPessoas com idade acima da média: ',end= ' ')
for i in Lista_Cadastro:
    if i['Idade'] >= (Med_idade/len(Lista_Cadastro)):
        for k,v in i.items():
            print(f'{k} = {v}', end=' ')
        print()
