"""
  * Programa para calcular uma divisão, caso o divisor seja 0, solicitar novo número. Após exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

dividendo  = float(input("Informe o dividendo: "))
divisor = 1

while not divisor == 0.0:
    divisor = float(input("Informe o divisor: "))
    if not divisor == 0.0:						  
        print("O valor da divisão é {:.2f}".format(dividendo / divisor))
	