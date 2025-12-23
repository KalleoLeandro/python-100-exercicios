"""
 * Programa para ler a idade de 2 casais, efetuar uma comparação e um cálculo e exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

idade_h1 = int(input("Informe a idade do primeiro homem: "))
idade_h2 = int(input("Informe a idade do segundo homem: "))
idade_m1 = int(input("Informe a idade da primeira mulher: "))
idade_m2 = int(input("Informe a idade da segunda mulher: "))


if idade_h1 > idade_h2 and idade_m1 > idade_m2:
    soma = idade_h1 + idade_m2
    produto = idade_h2 * idade_m1
elif idade_h1 > idade_h2 and idade_m1 < idade_m2:
    soma = idade_h1 + idade_m1
    produto = idade_h2 * idade_m2
elif idade_h1 < idade_h2 and idade_m1 > idade_m2:
    soma = idade_h2 + idade_m2
    produto = idade_h1 * idade_m1
else :
    soma = idade_h2 + idade_m1;
    produto = idade_h1 * idade_m2;

print(f"A soma das idades é de {soma}\nO produto das idades é de {produto}")


