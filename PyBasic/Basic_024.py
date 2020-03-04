Atleta = {}
Gols = list()
ContGol = 0
Atleta_list = list()

while True:
    Atleta['Nome'] = str(input('Nome do atleta:  '))
    Partidas= int(input('Quantidade de partidas em campo: '))
    for i in range(Partidas):
        Gols.append(int(input(f'Quantidade de gols no jogo {i+1}:  ')))
    Atleta['Gols'] = Gols[:]
    Atleta['Total de gols'] = sum(Gols)
    Atleta_list.append(Atleta.copy())
    Gols.clear()

    answer = input('Continuar ? [S/N]').strip().upper()[0]
    if answer in 'N':
        break
print(f'{"Atleta":^10}  {"Gols":^10}     {"Total de gols":^10}')
for p in Atleta_list:
    print(f'{p["Nome"]:^10}  {p["Gols"]}          {p["Total de gols"]}')


print(f'\n{Atleta_list}')