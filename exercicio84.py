"""
 * Programa receber indefinidamente o salário e o número de filhos da população. Após calcular a media salarial, a média de filhos, maior salári e percentual de habitantes baixo salário.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """
salario = 1
soma_salarios = 0
total_filhos = 0
maior = 0
contador = 0
qtd_salario_abaixo_1500 = 0

while salario > 0:
    salario = float(input("Informe o salário do habitante (<= 0 para sair): "))
    
    if salario > 0:
        soma_salarios += salario
        total_filhos += int(input("Informe o número de filhos do habitante: "))
        
        if salario > maior:
            maior = salario
            
        if salario < 1500:
            qtd_salario_abaixo_1500 += 1
        
        contador += 1

if contador > 0:
    media_salario = soma_salarios / contador
    media_filhos = total_filhos / contador
    percentual = (qtd_salario_abaixo_1500 / contador) * 100

    print(
        f"A média salarial da população é de R${media_salario:.2f}.\n"
        f"A média do número de filhos é {media_filhos:.2f} por habitante.\n"
        f"O maior salário registrado foi de R${maior:.2f}.\n"
        f"O percentual de pessoas com salário menor que R$1500,00 é de {percentual:.2f}%"
    )
else:
    print("Nenhum dado válido foi informado.")
