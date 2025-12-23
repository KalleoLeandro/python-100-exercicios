"""
 * Programa para verificar resultados e exibir em tela de acordo com uma comparação
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

time_a = input("Informe o nome do primeiro time: ")
time_b = input("Informe o nome do segundo time: ")

placar_a = int(input(f"Informe o placar do time {time_a}: "))
placar_b = int(input(f"Informe o placar do time {time_a}: "))

if placar_a> placar_b:
    print(f"Vencedor: {time_a}")
elif placar_b > placar_a:
    print(f"Vencedor: {time_b}")
else:
    print(f"Empate")

    


