"""
 * Programa para exibir a temperatura convertida de medida imperial para medida do Sistema internacional de acordo com valor informado pelo usuário  
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

fahrenheit = float(input("Informe o valor da temperatura em F°: "));

celsius = (5*fahrenheit - 160) / 9;	

print(f"A temperatura convertida em C° é de {celsius}");


