from Modularização.lib.arquivo import *
from time import sleep

arq = 'Cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Novo Cadastro')
        name = str(input('Nome: '))
        year = int(input('Idade: '))
        cadastrar(arq, name, year)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\33[31ERRO: Digite uma opção válida\033[m.')
    sleep(0.4)
