"""
 * Programa para ler 10 números e armazenar em um array os valores. Depois, receber um valor e verificar quantas vezes esse valor aparece no array. Imprimir a quantidade.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

numeros_a = []
numeros_b = []
qt = 0

for i in range(0, 11,1):    
    numeros_a.append(float(input(f"Informe o {i}° número: ")))

valor = float(input(f"Informe o {i}° número: "))

for i in range(0, len(numeros_a), 1):
     if numeros_a[i] == valor:
          qt += 1          


print(f"A quantidade de valores iguais a valor informado é de {qt}")