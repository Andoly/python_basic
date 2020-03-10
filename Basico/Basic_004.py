pythNum = 99999
pythNome = str(input('Nome completo : ')).upper().strip()

while pythNum > 9999:
    pythNum = int(input('Número de 0 a 9999 : '))

#print("Quantidade de 'o' : {}".format(pythNome.count('o')))     #Exibe a quantidade do caractere 'o'
#print(format(pythNome.find('Andoly')))                          #Exibe a posição inicial da string 'Andoly'
#print(format(pythNome.replace('Andoly','Maryana')))             #Modifica de forma temporária Andoly->Maryana
#print(format(pythNome.upper()))                                 #Todos caracteres maiúculo
#print((format(pythNome.lower())))                               #Todos caracteres minúsculo
#print(format(pythNome.capitalize()))                            #Somente o primeiro caractere minúsculo
#print(format(pythNome.title()))                                 #Início de cada string de forma maiúsuculo
#print(format(pythNome.strip()))                                 #Elimina espaços vazios desnecessario no vetor
#print(format(pythNome.lstrip()))                                #Elimina os espaços a esquerda
#print(format(pythNome.split()))                                 #Divide em lista de strings a partir de cada espaço ' '

aux0 = 'SILVA' in pythNome

if(aux0):
    print('{} possui  {} Silva no nome, contém {} caracteres sem contabilizar espaços'
          .format(pythNome.title(),pythNome.count('SILVA'),len(pythNome) - pythNome.count(' ') ))
else:
    print('{} possui não possui Silva, contém {} caracteres sem contabilizar espaços'
          .format(pythNome,len(pythNome) - pythNome.count(' ') ))

aux = pythNome.split()
print('Primeiro nome : {} com {} caracteres'.format(aux[0].title(),len(aux[0])))
print('Ultimo nome : {} com {} caracteres'.format(aux[len(aux)-1].title(), len(aux[len(aux)-1])))
print('Unidade  : {}'.format(pythNum % 10))
print('Dezena   : {}'.format((pythNum // 10) % 10))
print('Centena  : {}'.format((pythNum // 100) % 10))
print('Milhar   : {}'.format((pythNum // 1000)))



