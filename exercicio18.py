"""
 * Programa para exibir o percentual dos eleitores com os valores  recebido do usuário
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

eleitores = int(input("Informe o número total de eleitores: "))
brancos = int(input("Informe o número total de votos brancos: "))
nulos = int(input("Informe o número total de votos nulos: "))
validos = int(input("Informe o número total de votos validos: "))

brancos = (brancos/eleitores) * 100;
nulos = (nulos/eleitores) * 100;
validos = (validos/eleitores) * 100;

print(f"O percentual de votos brancos foi de {brancos}%\nO percentual de votos nulos foi de {nulos}%\nO percentual de votos validos foi de {validos}%");


