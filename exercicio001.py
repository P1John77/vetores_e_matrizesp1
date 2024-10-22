lista_de_times =['Flamengo', 'Vasco', 'Palmeiras','São paulo','Atletico MG'] 

verificador = input('digite o seu time do coraçao:')

confirmaçao_de_busca = False

for times in lista_de_times:

    if times.upper() == verificador.upper():
        confirmaçao_de_busca = True
if confirmaçao_de_busca:
    print('Achei!')
else:
    print('Nao achei!')            