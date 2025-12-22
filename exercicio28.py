"""
 * Programa para exibir o  valor a pagar individual dos 3 amigos, com restrições com base em valores informados pelo usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

total = float(input("Informe o valor total da comanda: "));

divisao = total / 3;

felipe = (int)(divisao);
carlos = (int)(divisao);
andre = (int)(divisao);

somainteira = felipe + carlos + andre;

resto = total - somainteira;
		
felipe = felipe + resto;

print(f"O valor que Felipe pagará é de R${felipe}\nO valor que Carlos pagará é de R${carlos}\nO valor que André pagará é de R${andre}");


