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

print('ID', end=' ')
for i in Atleta.keys():
    print(f'{i:<20}', end=' ')
print()

for k,v in enumerate(Atleta_list):
    print(f'{(k)} ', end=' ')
    for d in v.values():
        print(f'{str(d):<20}', end=' ')
    print()
print('-'* 40)
while True:
    search = int(input('Deseja visualizar dados de qual jogador? [999 - SAIR] : '))
    if search == 999:
        break
    if search >= len(Atleta_list):
        print(f'Não existe atleta com o código {search} digitado.')
    else:
        print(f'Status do atleta : {Atleta_list[search]["Nome"]}')
        for i, g in enumerate(Atleta_list[search]['Gols']):
            print(f'Jogo {i+1} {Atleta_list[search]["Nome"]} fez {g} gols')
        print()
