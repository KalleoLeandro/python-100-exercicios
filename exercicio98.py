"""
 * Programa para ler 30 números(15 para um array A e 15 parar um array B). Verificar a quantidade de vez que ambos os vetores possuem valores coincidentes , incluindo seus índices.   
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

numeros_a = []
numeros_b = []
qt = 0

for i in range(0, 11,1):    
    numeros_a.append(float(input(f"Informe o {i}° número: ")))

for i in range(0, 11,1):    
    numeros_b.append(float(input(f"Informe o {i}° número: ")))

for i in range(0, len(numeros_a), 1):
     if numeros_a[i] == numeros_b[i]:
          qt += 1
          print(f"Posição {i + 1}. Índice {i}. contém valor repetido")


print(f"A quantidade de valores repetidos em mesmas casas nos arrays é de {qt}")