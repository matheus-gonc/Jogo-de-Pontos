import random

linhas = 5
colunas = 6
matriz = []

dicionario_de_letras = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
}
lista_de_letras = list(dicionario_de_letras.keys())

# gerar a matriz e colocar números aleatórios nela
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = random.choice(lista_de_letras)
        linha.append(numero)
    matriz.append(linha)

#  contando a quantidade de vezes que os numeros aparecem 
for i in range(linhas):
    for j in range(colunas):
        dicionario_de_letras[matriz[i][j]] += 1


for i in matriz:
    print(i)
print('\n', dicionario_de_letras)

for chave in dicionario_de_letras:   # MOSTRANDO QUANTAS VEZES AS LETRAS APARECEM 
    print(f'A letra {chave} aparece {dicionario_de_letras[chave]} vezes')