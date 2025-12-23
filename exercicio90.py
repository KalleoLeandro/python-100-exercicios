"""
 * Programa para solicitar 20 números positivos e guardar em um array. Após, verificar o maior elemento e sua posição no vetor.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

numeros = []
maior = 0
posicao = 0
menor = 0

for i in range(0, 21,1):
    while menor <= 0:
        numeros[i].append(float(input(f"Informe o {i}° número: ")))

maior = numeros[0]

for i in range(0, len(numeros), 1):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i


if maior == 0:
    print(f" Todos os valores foram iguais a zero, logo a primeira ocorrência é no índice 0, na 1a posição do array")
else:
    print(f"O maior valor informado foi {maior}.\nSua primeira ocorrência está no índice {posicao}. Portanto ocupa a {i + 1}a posição do array")
