"""
 * Programa para calcular a media das notas de alunos, dado o número de alunos e as notas. Após, imprimir em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

alunos = 0
notas = 0

alunos = int(input("Informe o número de alunos da classe: "))

for i in range(1, alunos + 1,1):
    notas += float(input(f"Informe a nota do {i}° aluno: "))

print("A média aritmética da turma que contém {} alunos é {:.2f}".format(alunos, notas / alunos))