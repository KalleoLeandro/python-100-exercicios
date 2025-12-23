"""
 * Programa para calcular e exibir o saldo de um cliente
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

num_conta = int(input("Informe o número da conta"));
saldo = float(input("Informe o saldo atual"));
debito = float(input("Informe o débito"));
credito = float(input("Informe o crédito"));

	
saldo = saldo - debito + credito;
		
if saldo >=0:
	print(f"{saldo}")
	print(f"Número da conta {num_conta}\nSaldo positivo")
else:
	print(f"{saldo}")
	print(f"Número da conta {num_conta}\nSaldo negativo")
