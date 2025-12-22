"""
 * Programa para exibir a quantidade de dias passados do ano com base em valores informados pelo usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

dia = int(input("Informe o dia: "));
mes = int(input("Informe o mes: "));


mes = ((mes - 1) * 30) + dia;	

print(f"O número de dias que se passou desde o início do ano é de {mes}");


