"""
 * Programa para verificar a possibilidade de votação com base na idade e exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

ano = float(input("Informe o ano de nascimento de uma pessoa: "));

if 2025 - ano >=18:
    print(f"A pessoa poderá votar este ano")    
else:
    print(f"A pessoa não poderá votar este ano")    