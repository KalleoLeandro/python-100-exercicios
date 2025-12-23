"""
 * Programa para verificar um intervalo de tempo, e exibir o resultado em tela
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

hora_inicial = float(input("Informe a hora inicial do jogo de xadrez: "));
hora_final = float(input("Informe a hora final do jogo de xadrez: "));

horas = 0

if hora_final > hora_inicial:
	horas = hora_final - hora_inicial	
elif hora_inicial == hora_final:
    horas = 24;
else:
	horas = 24 - hora_inicial;
	horas = horas  + hora_final;

print(f"A duração da partida foi de {horas} horas")