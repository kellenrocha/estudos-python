def numElementos():
    lista_elementos = []
    elementos = int(input('Digite a quantidade de elementos da operação: '))

    if elementos < 2:
        print('Para realizar a operação é necessário mais de um valor... encerrando ')
    else:
        return elementos

def Soma():
    lista_elementos = []
    elementos = numElementos()
        
    for i in range(1, elementos + 1): #começar do 1º e ir um a mais, se o usuario digitar 3 irá [1,2,+1]
        lista_elementos.append(int(input(f'Digite o {i} º valor: ')))

    Tsoma = sum(lista_elementos)
    print('Total da Soma: ', Tsoma)

def Subtracao():
    lista_elementos = []
    elementos = numElementos()
        
    for i in range(1, elementos + 1): 
        lista_elementos.append(int(input(f'Digite o {i} º valor: ')))

    Tsubtracao = lista_elementos[0] #ja recebe o primeiro elemento
    for x in lista_elementos[1:]: #itera a partir do segundo elemento
        Tsubtracao -= x
    print('Total da Subtração: ', Tsubtracao)

def Multiplicacao():
    lista_elementos = []
    elementos = numElementos()

    for i in range(1, elementos + 1):
        lista_elementos.append(int(input(f'Digite o {i} º valor: ')))

    Tmultiplicacao = lista_elementos[0]
    for x in lista_elementos[1:]:
        Tmultiplicacao *= x
    print('Total da Multiplicação: ', Tmultiplicacao)

def Divisao():
    lista_elementos = []
    elementos = numElementos()

    for i in range(1, elementos + 1):
        lista_elementos.append(int(input(f'Digite o {i} º valor: ')))

    Tdivisao = lista_elementos[0]
    for x in lista_elementos[1:]:
        Tdivisao /= x
    
    print('Total da Divisão: ', Tdivisao)

#--------------------------------------------------------------------------------------


print()
print("******************* Calculadora em Python *******************")
print()
print('Selecione o número da operação desejada:')
print()
print(" 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão")
print()

operacao = int(input('Digite sua opção (1/2/3/4): '))
#elementos = input('Digite a quantidade de elementos da operação: ')

if operacao == 1:
    Soma() 
elif operacao == 2:
    Subtracao()
elif operacao == 3: 
    Multiplicacao()
elif operacao == 4:
    Divisao()
else: 
    print('Entrada inválida')


