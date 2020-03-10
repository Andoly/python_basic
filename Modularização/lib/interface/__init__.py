def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Digite uma opção válida.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31m Interrompido pelo usuário.\033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-'*tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Menu Principal')
    count = 1
    for item in lista:
        print(f'{count} - {item}')
        count +=1
    print(linha())
    opc = leiaInt('Sua opção : ')
    return opc
