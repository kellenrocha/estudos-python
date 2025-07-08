def Soma():
    lista_elementos = []
    elementos = int(input('Digite a quantidade de elementos da Soma: '))
    
    
    if elementos < 2:
        print('Para realizar a operação é necessário mais de um valor... encerrando ')
    else:
        for i in range(1, elementos + 1):
            lista_elementos.append(int(input(f'Digite o {i} º valor: ')))

        Tsoma = 0
        for x in lista_elementos:
            Tsoma = Tsoma + x
        print('Total da Soma: ', Tsoma)


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
    print('Subtração')
elif operacao == 3: 
    print('Multiplicação')
elif operacao == 4:
    print('Divisão')
else: 
    print('Entrada inválida')


