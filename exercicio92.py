"""
 * Programa para ler 10 números e guardar em um array.Depois, receber um valor e criar um vetor que contera o primeiro vetor multiplicado pelo valor. Imprimir o segundo vetor
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

numeros_a = []
numeros_b = []

for i in range(0, 11,1):    
    numeros_a.append(float(input(f"Informe o {i}° número: ")))

valor = int(input(f"Informe um valor: "))

for i in range(0, 11,1):    
    numeros_b.append(numeros_a[i] * valor)

for i in range(0, len(numeros_b),1):
    print(f"Posição {i + 1}: {numeros_b[i]}")
