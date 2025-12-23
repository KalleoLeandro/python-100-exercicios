"""
 * Programa para ler 10 valores e verificar o maior e o menor valor lido
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

num = 0
num = float(input(f"Informe um número: "))
maior = num
menor = num


for i in range(1,10,1):
    num = float(input(f"Informe um número: "))
    if maior < num:
        maior = num
    if menor > num:
        menor = num

if maior == menor:
    print("Só foram digitados valores iguais: {:.2f}".format(num))
else:
    print("O maior valor é{:.2f}.\nO menor valor é {:.2f}".format(maior, menor))