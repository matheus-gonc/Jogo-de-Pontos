import random

linhas = 5
colunas = 6
matriz = []

dicionario_de_numeros = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}
lista_de_numeros = list(dicionario_de_numeros.keys())

# gerar a matriz e colocar números aleatórios nela
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = random.choice(lista_de_numeros)
        linha.append(numero)
    matriz.append(linha)

for i in range(linhas):
    for j in range(colunas):
        dicionario_de_numeros[matriz[i][j]] += 1








for i in matriz:
    print(i)
print('\n', dicionario_de_numeros)