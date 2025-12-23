"""
 * Programa para ler valor e criar tres arrays de tamanho igual ao valor. Receber valores para o primeiro e o segundo e armazenar no terceiro a soma dos dois primeiros.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

numeros_a = []
numeros_b = []
numeros_c = []

for i in range(0, 11,1):    
    numeros_a.append(float(input(f"Informe o {i}° número: ")))

for i in range(0, 11,1):    
    numeros_b.append(float(input(f"Informe o {i}° número: ")))

for i in range(0, 11,1):    
    numeros_c.append(numeros_a[i] + numeros_b[i])


for i in range(len(numeros_c), -1,-1):        
    print(f"Posição {i + 1}: {numeros_a[i]}")
