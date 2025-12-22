"""
 * Programa para exibir a idade de uma pessoa em dias com os valores  recebido do usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

anos = int(input("Informe a idade em anos: "))
meses = int(input("Informe o restante da idade em meses: "))
dias = int(input("Informe o restante da idade em meses: "))

total = (anos * 365) + (meses * 12) + dias; 

print(f"A idade dessa pessoa em dias é {total}")


