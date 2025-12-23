"""
 * Programa para calcular a media ponderada de um aluno e exibir um resultado de acordo com uma comparação em tela  
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

n1 = float(input("Informe a primeira parcial"))
n2 = float(input("Informe a segunda parcial"))
n3 = float(input("Informe a terceira parcial"))
me = float(input("Informe a média dos exercícios"))


media = (n1 + n2*2 + n3*3 + me) / 7

if media >= 9:
    print(f"Conceito A")
elif media <= 7.5 and media < 9:
    print(f"Conceito B")
elif media <= 6.0 and media < 7.5:
    print(f"Conceito C")
else:
    print(f"Conceito D")