"""
 * Programa para ler as notas de 20 alunos e guardar em um array. Após, calcular a média de notas e quantas notas estiveram acima da média.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

notas = []
media = 0
maiores = 0

for i in range(0,20,1):
    notas.append(float(input(f"Informe um nome: ")))
    media += notas[i]

media /= len(notas)

for i in range(0,len(notas),1):
    if notas[i] > media:
        maiores += 1

print("A média da classe é {:.2f}.\nO total de alunos acima da média é {:.2f}".format(media, maiores))

