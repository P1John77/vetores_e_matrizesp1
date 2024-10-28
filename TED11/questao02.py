#Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos. Depois:

import random

#Imprima o resultado da soma de todos os valores da matriz no terminal;
A = [[random.randint(1,100) for _ in range(10)] for _ in range (10)]

print('Matriz A:')

for linha in A:
    print(linha)

soma_total = sum(sum(linha) for linha in A)
print(f'\nSoma de todos os valores da matriz A: {soma_total}')

#E, crie uma nova matriz B, no qual cada item seja o valor da matriz A * 3;
B = [[valor * 3 for valor in linha] for linha in A]
print('\nMatriz b (cada elemento e o valor correspondente de A * 3):')

for linha in B:
    print(linha)