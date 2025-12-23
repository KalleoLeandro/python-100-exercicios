"""
 * Programa para ler 10 números, armazenar o mesmos em um array e ordenar o array. Imprimir o array ordenado.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

numeros_a = []

for i in range(0, 11,1):    
    numeros_a.append(float(input(f"Informe o {i}° número: ")))

for i in range(0,len(numeros_a), 1):
	for j in range(0,len(numeros_a) - 1, 1):
		if(numeros_a[j] > numeros_a[j + 1]):
			aux = numeros_a[j];
			numeros_a[j] = numeros_a[j+1];
			numeros_a[j+1] = aux;

for i in range(0, len(numeros_a), 1):
	print(f"{numeros_a[i]}")