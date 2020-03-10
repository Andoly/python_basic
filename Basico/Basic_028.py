def leiaInt():
    while True:
        try:
            entrada = int(input('Digite um número inteiro: '))
            break
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')
    return entrada

print(leiaInt())

def notas(*notas, Situação =False):
    """
    :param notas: Recebe uma lista de notas para analise
    :param Situação: Classificação da nota a partir da média
    :return: Dicionário com quantidade de notas, maior, menor, média e situação
    """
    planilha = dict()
    planilha['Quantidade'] = len(notas)
    planilha['Maior'] = max(notas)
    planilha['Menor'] = min(notas)
    planilha['Média'] = f'{(sum(notas)/len(notas)):.2f}'
    Mid = (sum(notas)/len(notas))
    if Situação:
        if Mid >= 8:
            planilha['Situação'] = 'Rendimento bom'
        elif Mid >= 6:
            planilha['Situação'] = 'Rendimento médio'
        else:
            planilha['Situação'] = 'Rendimento ruim'
    return planilha

def analise():
    medias = notas(9.6, 5, 6.8, 7.5, 8.3, 10, 9.2, 6, Situação=True)
    print(medias)

analise()

