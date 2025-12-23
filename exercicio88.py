"""
 * Programa para ler 10 nomes e armazenar em um array, depois, deverá receber um nome e procurar em um array. Imprimir se achou ou não o nome igual.
 * @author Kalleo Leandro dos Santos Leal
 * @since 22/12/2025
 """

nomes = []

for i in range(0,11,1):
    nomes.append(input(f"Informe um nome: "))

nome_busca = input(f"Informe um nome a buscar: ")

for i in range(0,len(nomes),1):
    if nomes[i] == nome_busca:
        contem = True

if contem:
    print(f"Achou")
else:
    print(f"Não achou")