"""
 * Programa para verificar as notas dos alunos e exibir uma mensagem em tela de acordo com o resultado
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

m1 = float(input("Informe a primeira parcial: "));
m2 = float(input("Informe a segunda parcial: "));

media = (m1 + m2) /2;

	
if media >=6:
    print(f"O aluno foi aprovado")    
else:
    print(f"O aluno foi reprovado")    