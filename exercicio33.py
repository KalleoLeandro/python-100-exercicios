"""
 * Programa para calcular e exibir o total de reais, conforme o número de moedas e seus valores informados pelo usuário    
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

um = int(input("Informe o número de moedas de R$0,01"));
cinco = int(input("Informe o número de moedas de R$0,05"));
dez = int(input("Informe o número de moedas de R$0,10"));
vinte_cinco = int(input("Informe o número de moedas de R$0,25"));
cinquenta = int(input("Informe o número de moedas de R$0,50"));
um_real = int(input("Informe o número de moedas de R$1,00"));


total = (um*0.01) + (cinco*0.05) + (dez*0.1) + (vinte_cinco*0.25) + (cinquenta*0.5) + um_real;   


print(f"O valor total em reais economizado é de R$ {total}")

