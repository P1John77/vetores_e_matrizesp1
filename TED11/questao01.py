#Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

VET = []

for i in range(10):
    num = int(input(f'digite o numero {i + 1}:'))
    VET.append(num)

repetidos = {}


for i in range(len(VET)):
    numero = VET[i]
    if VET.count(numero) > 1:
        if numero not in repetidos:
            repetidos[numero] = []
        repetidos[numero].append(i)


if repetidos:
    print('\nNumeros repetidos e suas posiçoes:')
    for numero, posiçoes in repetidos.items():
        print(f'numero {numero}encontrado nas posiçoes: {posiçoes}')

    else:
        print('\nNao há numeros repetidos no vetor.')                