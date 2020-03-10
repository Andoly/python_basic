from Modularização.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except FileNotFoundError:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro na leitura do arquivo.')
    else:
        cabeçalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:<3} anos')
    finally:
        a.close()

def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro no momento de cadastrar dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()




