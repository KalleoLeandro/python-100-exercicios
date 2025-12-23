"""
 * Programa para calcular a quantidade média e exibir um resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

qt_atual = int(input("Informe a quantidade atual em estoque de um produto"));
qt_min = int(input("Informe a quantidade mínima de estoque de um produto"));
qt_max = int(input("Informe a quantidade máxima de estoque de um produto"));
		
qt_media = (qt_max + qt_min) /2;		
		
if qt_atual > qt_media:
	print(f"Não efetuar compra");
else:
	print(f"Efetuar compra");
