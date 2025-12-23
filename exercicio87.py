"""
 * Programa para imprimir um retângulo 10 x 60 caracteres na tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

retangulo = ""


for linha in range(1,11,1):
    for coluna in range(1,61,1):
        if linha == 1 or linha == 10:
            retangulo += "+"
        elif coluna == 1 or coluna == 60:
            retangulo += "+"
        else:
            retangulo += " "
    retangulo += "\n"

print(f"{retangulo}")

