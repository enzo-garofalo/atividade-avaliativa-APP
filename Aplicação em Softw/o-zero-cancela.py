print(f"\n\tBem vindo(a) ao zero cancela.")

# inicialização de variáveis
num_atual = soma = ant1 = ant2 = ant3 = nums_considerados = nums_desconsiderados = zeros_consecutivos = 0

while num_atual >= 0: 

    # Solicita ao usuário um número e armazena na variável num_atual
    num_atual = float(input(f"\nNúmero: "))

    if num_atual > 0:
        # Se sim, ele é considerado na soma e incrementa o valor números considerados
        soma += num_atual
        print(f"Soma dos números adicionados: {soma}")
        nums_considerados += 1

        # Atualiza o histórico dos três últimos números digitados
        ant3 = ant2
        ant2 = ant1
        ant1 = num_atual

        # Reinicia o contador de zeros consecutivos
        zeros_consecutivos = 0

    # Verifica se o número digitado é igual a zero
    elif num_atual == 0:

        # Incrementa o contador de zeros consecutivos 
        zeros_consecutivos += 1 

        # Se sim, verifica se já houve três zeros consecutivos
        if zeros_consecutivos > 3:
            print(f"Só é possível digitar 3 zeros consecutivos!")
        elif ant1 > 0:
            
            # Se não, subtrai o último número considerado da soma
            soma -= ant1

            # incrementa o contador de números desconsiderados e decrementa o considerado 
            nums_desconsiderados += 1
            nums_considerados -= 1

            # Atualiza o histórico dos três últimos números digitados
            ant1 = ant2
            ant2 = ant3
            ant3 = 0 

            print(f"Nova soma: {soma} | Número desconsiderado: {ant1}")
        else:
          print(f"Soma dos números adicionados: {soma}")
          print(f"Não é possisvel desconsiderar nenhum número da soma!\n")
            
print(f"\n\tZero cancela interrompido por {num_atual}\n |Soma = {soma}\n |Números considerados: {nums_considerados}\n |Números desconsiderados: {nums_desconsiderados}")