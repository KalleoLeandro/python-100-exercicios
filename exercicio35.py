"""
 * Programa para calcular e exibir a idade de uma pessoa em diferentes medidas de tempo com base nos valores informados pelo usuário  
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

anonascimento = int(input("Informe o ano de nascimento de uma pessoa "));
anoatual = int(input("Informe o ano atual"));		

idade = anoatual - anonascimento;
semanas = idade * 52;
meses = idade * 12;
dias = idade * 365;

print(f"A idade dessa pessoa em anos é {idade}\nA idade dessa pessoa em meses é {meses}\nAidade dessa pessoa em dias é {dias}\nA idade dessa pessoa em semanas é {semanas}")

