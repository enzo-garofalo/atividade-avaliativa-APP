#  Construir um programa que calcule a soma de uma sequencia de números digitado pelo usuário, 
#  Quando o usuário digitar 0 vai cancelar o último digito, o usuário pode cancelar 3 vezes consecutivas
# O programa deve exibir soma total, números considerados e números desconsiderados
#  O programa vai parar quando num < 0 

print(f"\n\tBem vindo(a) ao zero cancela.")

num = soma = num_anterior1 = num_anterior2 = num_anterior3 = zero_consecutivo = 0
qtd_num = 1

while True:
    num = float(input("Número: "))

    if num < 0:
        break

    elif num > 0: 
        soma += num
        num_anterior3 = num_anterior2
        num_anterior2 = num_anterior1
        num_anterior1 = num
        continue

    elif num == 0:
        # Laço para zeros consecutivos
       if zero_consecutivo >= 3:
           print("Só é permitido 3 números consecutivos!!!")
           continue
       elif zero_consecutivo == 0:
           soma -= num_anterior1
           zero_consecutivo += 1
           continue
       elif zero_consecutivo == 1:
           soma -= num_anterior2
           zero_consecutivo += 1
           continue
       elif zero_consecutivo == 2:
           soma -= num_anterior3
           zero_consecutivo += 1
           continue
    
print(f"Soma total = {soma}")