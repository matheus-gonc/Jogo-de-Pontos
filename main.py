import random

linhas = 5
colunas = 6
matriz = []

dicionario_de_letras = {
    'A': [0, 0.25, 0.75, 2],
    'B': [0, 0.4, 0.9, 4],
    'C': [0, 0.5, 1, 5],
    'D': [0, 0.8, 1.2, 8],
    'E': [0, 1, 1.5, 10],
    'F': [0, 1.5, 2, 12],
    'G': [0, 2, 5, 15],
    'H': [0, 2.5, 10, 25],
    'I': [0, 10, 25, 50 ],
}
lista_de_letras = list(dicionario_de_letras.keys())

pontos_por_letras = []

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
        dicionario_de_letras[matriz[i][j]][0] += 1

for i in matriz:
    print(i)
print('\n', dicionario_de_letras)

for chave in dicionario_de_letras:   # MOSTRANDO QUANTAS VEZES AS LETRAS APARECEM 
    print(f'A letra {chave} aparece {dicionario_de_letras[chave][0]} vezes')

    ocorrencia = dicionario_de_letras[chave][0]
    if ocorrencia >= 7:
        pontuacao = ocorrencia * dicionario_de_letras[chave][3]
    elif ocorrencia == 6:
        pontuacao = ocorrencia * dicionario_de_letras[chave][2]
    elif ocorrencia == 5:
        pontuacao = ocorrencia * dicionario_de_letras[chave][1]
    else:
        pontuacao = 0
    pontos_por_letras.append(pontuacao)
print(pontos_por_letras)

total_pontos = 0
for i in pontos_por_letras:
    total_pontos += i
print(total_pontos)
