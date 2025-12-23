"""
 * Programa para ler 20 números e armazenar em um array. Depois, imprimir na ordem inversa em que foram recebidos.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

numeros_a = []

for i in range(0, 11,1):    
    numeros_a.append(float(input(f"Informe o {i}° número: ")))

for i in range(len(numeros_a), -1,-1):        
    print(f"Posição {i + 1}: {numeros_a[i]}")
