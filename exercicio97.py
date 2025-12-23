"""
 * Programa Receber um conjunto de 20 números. Depois receber mais um número e comparar com os valores do array. Caso o número exista, criar um novo array sem o valor recebido.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

numeros_a = []

for i in range(0, 11,1):    
    numeros_a.append(float(input(f"Informe o {i}° número: ")))

num = (float(input(f"Informe mais um número: ")))

nums = [x for x in numeros_a if x != num]

for i in range(0, len(numeros_a), 1):
	print(f"{numeros_a[i]}")