# Exemplo 1
# Restrição : Verificar impar ou par, somente após carregar uma lista


listaGeral = list()
listaPares = list()
listaImpares = list()
while True:
    listaGeral.append(int(input('Digite um número : ')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(listaGeral):
    if v % 2 == 0:
        listaPares.append(v)
    elif v % 2 == 1:
        listaImpares.append(v)

print(f'\nLista completa : {listaGeral}')
print(f'Lista de pares : {listaImpares}')
print(f'Lista de impares : {listaPares}\n')


# Exemplo 2
expressao = str(input('Digite uma expressão :'))
Pilha = []
for simb in expressao:
    if simb == '(':
        Pilha.append('(')
    elif simb == ')':
        if len(Pilha) > 0:
            Pilha.pop()
        else:
            Pilha.append('#')
            break
if len(Pilha) == 0:
    print('Sintaxe da expressão é válida')
else:
    print('Sintaxe da expressão é invalida')


