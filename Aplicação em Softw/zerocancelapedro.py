
# QUER:
#  um programa que calcule a soma de uma sequência de números digitados pelo usuário
#  Digite zero para desconsiderar o último número digitado
#  O usuário pode digitar até 3 vezes consecutivamente o zero para desconsiderar os três últimos números digitados
#  A inserção é finalizada quando um número negativo é digitado ###

print("\nBem vindo(a) ao Zero Cancela!")

numero = 0
soma = 0
numero_anterior_1 = 0
numero_anterior_2 = 0
numero_anterior_3 = 0
contador_de_zeros = 0

for i in range(999999):  
    numero = int(input("\nDigite um número: "))
    soma = soma + numero
    if numero < 0:
        break
    print(f"{numero}")

    if numero == 0:
        numero = numero_anterior_1 = 0

    if numero_anterior_1 == 1:
        numero_anterior_2 =+1
    if numero_anterior_2 == 1:
        numero_anterior_3 =+1
    if numero_anterior_3 == 1:
        print("Só é permitido até 03 zeros consecutivos!!")
    numero = int(input("Digite um número: "))

print(soma)
    