"""
 * Programa para calcular e exibir o total em agua e suco necessários para fazer um refresco, com base nos valores informados pelo usuário    
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

litros = float(input("Informe o total de litros de refresco a serem produzidos "));


agua = litros * 0.8;
suco = litros * 0.2;


print(f"São necessários {agua} litros de agua e {suco} litros de suco para produzir a quantidade de {litros} litros de refresco")

