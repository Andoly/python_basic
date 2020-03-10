from datetime import datetime

RH = {}
Cadastro = list()

while True:
    RH['Nome'] = str(input(f'Funcionário : ')).strip()
    Nasc = int(input('Ano nascimento: '))
    RH['Idade'] = datetime.now().year - Nasc
    RH['Ctps'] = str(input('Número CTPS, [dígite 0 caso não tenha]: ')).strip()[0]
    if RH['Ctps'] != '0':
        RH['Contratação'] = int(input('Ano de contratação: '))
        RH['Salario'] = float(input('Salário: '))
        RH['Aposentadoria'] = ((RH['Contratação'] + 35) - Nasc)
    elif RH['Ctps'] == '0':
        RH['Ctps'] = ' '
        RH['Contratação'] = ' '
        RH['Salario'] = ' '
        RH['Aposentadoria'] = ' '

    Cadastro.append(RH.copy())
    answer = str(input('Continuar ? [S/N]')).strip().upper()
    if answer in 'N':
        break
print(f'\n-=-=-=-=-=-=-=-=-=-= Funcionários =-=-=-=-=-=-=-=-=-=-=')
print(f'{"Nome":^7} | {"Idade":^7} | {"CTPS":^7} | {"Salário":^7} | {"Aposentadoria":^7}')

for i in range(0,len(Cadastro)):
    print(f'{Cadastro[i]["Nome"]:^7} | {Cadastro[i]["Idade"]:^7} | {Cadastro[i]["Ctps"]:^7} | '
          f'{Cadastro[i]["Salario"]:^7} | {Cadastro[i]["Aposentadoria"]:^7}')





