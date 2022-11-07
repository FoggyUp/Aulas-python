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

candidato1 = 0
candidato2 = 0

print('''
Candidato Paulo Freire = 10
Candidato Jean Piaget = 20
''')

voto = int(input('Digite seu voto!: '))
if voto == 10:
    candidato1 += 1
        
if voto == 20:
    candidato2 += 1
        
print(f'A soma dos votos de Paulo Freire é de: {candidato1} A soma dos votos de Jean Piaget é de: {candidato2}')