#  Construir um programa que calcule a soma de uma sequencia de números digitado pelo usuário, 
#  Quando o usuário digitar 0 vai cancelar o último digito, o usuário pode cancelar 3 vezes consecutivas
# O programa deve exibir soma total, números considerados e números desconsiderados
#  O programa vai parar quando num < 0 

print(f"\n\tBem vindo ao zero cancela.")

num = soma = num_anterior1 = num_anterior2 = num_anterior3 = 0
qtd_num = 1

while num >= 0:
    num = float(input("Número: "))


    if num > 0:
        soma += num
        conta_zero = 0

        while qtd_num <= 3:
            if qtd_num == 1:
                num_anterior1 = num
                qtd_num += 1
                break

            elif qtd_num == 2:
                num_anterior2 = num
                qtd_num += 1
                break

            elif qtd_num == 3:
                num_anterior3 = num
                qtd_num = 1
                break

    # for i in range(0,num,3):
    #     print(i)

    elif num == 0:
        # Laço para zeros consecutivos
        while conta_zero <= 3:

            if conta_zero == 0:
                conta_zero += 1
                soma -= num_anterior3
                break

            elif conta_zero == 1:
                soma -= num_anterior2
                conta_zero += 1
                break

            elif conta_zero == 2:
                soma -= num_anterior1
                conta_zero += 1
                break

            elif conta_zero >=3:
                print("Só é permitido até 03 zeros consecutivos!!")
                break

        
print(f"Soma total = {soma}")