"""
 * Programa para calcular e exibir o total de litros de refrigerante adquiridos com base nos valores informados pelo usuário   
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

lata350 = int(input("Informe o número de latas de 350ml adquiridos: "));
garrafa600 = int(input("Informe o número garrafas de 600ml adquiridos"));
garrafa2l = int(input("Informe o número garrafas de 2l adquiridos"));
		

lata350 = lata350 * 0.350;
garrafa600 = garrafa600 * 0.6;
garrafa2l = garrafa2l * 2;
    
		
total = lata350 + garrafa600 + garrafa2l;

print(f"O valor total de litros adquiridos é de {total}")

