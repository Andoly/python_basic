# Exemplo 1
def fatorial(num=1, show=False):
    from time import sleep
    """
    :param num: Recebe o número para operação fatorial
    :param show: Recebe um valor lógico opcional 
    :return: Fatorial do número passado
    """
    f = 1
    for c in range(num, 0 , -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
            sleep(0.3)
        f *= c
    return f

def Factorial_Call():

    print('Fatorial de N\n')
    n = int(input('Número para operação fatorial : '))
    print(f'{fatorial(n,True)}')

# Exemplo 2
def voto(nasc):
    """
    :param nasc: Recebe a data de nascimento
    :return: Idade atual
    """
    from datetime import date
    Idade = date.today().year - nasc
    if Idade < 16:
        return f'Com {Idade} anos, não permite votar'
    elif 16 <= Idade < 18 or Idade > 65:
        return f'Com {Idade} anos, voto opcional'
    elif Idade >= 18:
        return f'Com {Idade} anos, voto obrigatório'

def verificaVoto():
    print('\nVerificando obrigatoriedade do voto')
    year = int(input('Ano de nasc. p/ verificação de voto : '))
    print(voto(year))

# Exemplo 3
def ficha(Nome = False, XGols = 0):
    """
    :param Nome: Nome do atleta, pré definido como 'False' se vazio
    :param XGols: Quant. de gols, pré definida como 0, se vazio
    :return: Nome e quantidade de gols
    """
    if Nome:
        if XGols:
            return f'{Nome} fez {XGols} gol(s) no campeonato'
    else:
        if XGols:
            return f'<desconhecido> fez {XGols} gol(s) no campeonato'
        else:
            return f'<desconhecido> fez {XGols} gol(s) no campeonato'

def Atleta():
    print('\nRendimento do atleta')
    Jogador = str(input('Nome do atleta : '))
    try:
        Gols = int(input(f'Quantidade de gols marcados pelo {Jogador} : '))
    except ValueError:
        Gols = 0

    print(ficha(Jogador,Gols))

Factorial_Call()
verificaVoto()
Atleta()