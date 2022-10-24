doc = int(input('''
 1 - Para RG 
 2 - Para Título
Digite o tipo de documento:'''))
 
if doc == 1:
    rg = int(input('Digite o número do RG:'))
    if rg == 12345678:
        print('Pode Votar!')
        print('João do Carmo')
    else:
        print('Eleitor não encontrado')

if doc == 2:
    titulo = int(input('Digite o número do Título:'))
    if titulo == 11122233344:
        print('Pode Votar!')
        print('João do Carmo')
    else:
        print('Eleitor não encontrado')


