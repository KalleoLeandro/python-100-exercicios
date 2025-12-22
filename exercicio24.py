"""
 * Programa para exibir aa media final ponderada de acordo com os valores fornecidos pelo usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

n1 = float(input("Informe a primeira parcial: "));
n2 = float(input("Informe a segunda parcial: "));
n3 = float(input("Informe a terceira parcial: "));

media = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10; 

print(f"A média final do aluno é {media}");


