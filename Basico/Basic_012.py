
Br19 = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-Pr','São Paulo','Internacional','Corinthians','Fortaleza',
        'Goiás','Bahia','Vasco','Atlético-Mg','Fluminense','Botafogo','Ceará','Cruzeiro','Csa','Chapecoense','Avaí')

Pontuação_Br19 = ('90','74','74','65','64','63','57','56','53','52','49','49','48','46','43','39','36','32','32','20')

i = 0

print('\nTOP 5 BRASILEIRÃO 2019')
# Outra forma seria usando : print(f' TIME :  :  : {Br19[0:5]}')
for i in range(0,5):
    print(f'{i+1}º {Br19[i]} clube na classificação')
print('\nREBAIXADOS DO BRASILEIRÃO 2019')

# Outra forma seria usando : print(f' TIME :  :  : {Br19[-4:]}')
for i in range(16,20):
     print(f'{i+1}º {Br19[i]} clube na classificação')

print(f'\nTimes em ordem alfabetica : {sorted(Br19)}')

while True:
    time = str(input('Time : ')).title()
    if time in Br19:
        break
print(f'\n{time} está na {Br19.index(time)+1}º posição com {Pontuação_Br19[Br19.index(time)]}')

