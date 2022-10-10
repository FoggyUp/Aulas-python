n1 = int(input("Digite a 1° nota: "))
n2 = int(input('Digite a 2° nota:'))
n3 = int(input('Digite a 3° nota:'))
n4 = int(input('Digite a 4° nota:'))
soma = n1 + n2 + n3 + n4
media = soma / 4
print("Media final",media)
if media < 6.0:
    print('Reprovado')
else:
    print('Aprovado')