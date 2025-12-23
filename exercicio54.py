"""
 * Programa para ler 3 valores e verificar se é ou não um triângulo, e exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

a = float(input("Informe o primeiro lado: "))
b = float(input("Informe o segundo lado: "))
c = float(input("Informe o terceiro lado: "))

if a + b > c and b+c > a and  a +c  > b:
    print(f"A,B e C são lados de um triângulo")
else:
    print(f"A,B e C não são lados de um triângulo")
    


