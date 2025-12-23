"""
 * Programa para ler 10 valores e verificar a quantidade de valores no intervalo fechado de 10 a 20. Após, imprimir a quantidade em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

negativos = 0

for i in range(1,11,1):
    valor = float(input("Informe um número: "))
    if valor < 0:        
        negativos += 1
    

print(f"O total de números negativos é {negativos}")