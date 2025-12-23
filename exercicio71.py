"""
 * Programa para receber um valor informado pelo usuário e calcular a tabuada deste valor
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

n = int(input("Informe um número: "))

for i in range(1,11,1):
    print(f"{i * n}")