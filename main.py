import random

linhas = 5
colunas = 6
matriz = []

lista_de_numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
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

# gerar a matriz e colocar números aleatórios nela
for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = random.choice(lista_de_numeros)
        linha.append(numero)
    matriz.append(linha)




for i in matriz:
    print(i)