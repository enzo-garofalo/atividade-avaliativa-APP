#  Construir um programa que calcule a soma de uma sequencia de números digitado pelo usuário, 
#  Quando o usuário digitar 0 vai cancelar o último digito, o usuário pode cancelar 3 vezes consecutivas
# O programa deve exibir soma total, números considerados e números desconsiderados
#  O programa vai parar quando num_atual < 0 

print(f"\n\tBem vindo ao zero cancela.")
# inicialização de variáveis
num_atual = soma = num_anterior1 = num_anterior2 = num_anterior3 = nums_considerados = nums_desconsiderados = 0

# Laço que continuará enquanto o número digitado pelo usuário for maior ou igual a zero
while num_atual >= 0:
    
    # Solicita ao usuário um número e armazena na variável num_atual
    num_atual = float(input("Número: "))
    

    if num_atual > 0:
        # Se sim, ele é considerado na soma e incrementa o valor números considerados
        soma += num_atual
        nums_considerados += 1

        # Atualiza o histórico dos três últimos números digitados
        num_anterior3 = num_anterior2
        num_anterior2 = num_anterior1
        num_anterior1 = num_atual

        # Reinicia o contador de zeros consecutivos
        zero_consecutivo = 0
    
    # Verifica se o número digitado é igual a zero
    elif num_atual == 0:
        # Se sim, verifica se já houve três zeros consecutivos
        if zero_consecutivo == 3:
            print("Apenas 3 zeros consecutivos.")
        else:
            # Se não, incrementa o contador de números desconsiderados e decrementa o considerado
            nums_desconsiderados += 1
            nums_considerados -= 1

            # Subtrai o último número considerado da soma
            soma -= num_anterior1 
            
             # Atualiza o histórico dos três últimos números digitados
            num_anterior1 = num_anterior2
            num_anterior2 = num_anterior3
            num_anterior3 = 0

             # Incrementa o contador de zeros consecutivos 
            zero_consecutivo += 1 

# Verifica se não houve números considerados na soma                
if nums_considerados <=  0:
    nums_considerados = 0
    soma = 0

# Imprime os resultados
print(f"Soma = {soma}")
print(f"Numeros considerados: {nums_considerados}")
print(f"Numeros desconsiderados: {nums_desconsiderados}")