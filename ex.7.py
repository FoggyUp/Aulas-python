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
        
    candidato = print('''
CANDIDATO 1: Paulo Freire
CANDIDATO 2: Jean Piaget''' )

candidato1 = "Paulo Freire"
candidato2 = "Jean Piaget"

voto = int(input('Digite o número do seu Candidato a Presidencia:'))
if voto == 20:
    print('Candidato', candidato2)
elif voto == 10:
    print('Candidato', candidato1)

      




 