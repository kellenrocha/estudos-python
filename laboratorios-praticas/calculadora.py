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
    print('Soma')
    lista_elementos = []
    elementos = int(input('Digite a quantidade de elementos da operação: '))
    for i in range(1, elementos + 1):
        lista_elementos.append(input(f'Digite o {i} º valor: '))
    #print(lista_elementos)
elif operacao == 2:
    print('Subtração')
elif operacao == 3: 
    print('Multiplicação')
elif operacao == 4:
    print('Divisão')
else: 
    print('Entrada inválida')
