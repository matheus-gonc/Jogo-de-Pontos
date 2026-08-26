import random

def obter_tabela_letras(): #criação do dicionário de letras
    return {
        'I': [0, 0.25, 0.75, 2],
        'H': [0, 0.4, 0.9, 4],
        'G': [0, 0.5, 1, 5],
        'F': [0, 0.8, 1.2, 8],
        'E': [0, 1, 1.5, 10],
        'D': [0, 1.5, 2, 12],
        'C': [0, 2, 5, 15],
        'B': [0, 2.5, 10, 25],
        'A': [0, 10, 25, 50],
        '#': [0, 2]
    }

def gerar_matriz(linhas, colunas, lista_de_letras): # gera a matriz e colocar letras aleatórias nela
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            letra = random.choice(lista_de_letras) # todas as string tem a mesma chance de serem sorteadas
            linha.append(letra)
        matriz.append(linha)
    return matriz

def contar_ocorrencias(matriz, dicionario_de_letras, linhas, colunas): # contando a quantidade de vezes que as letras aparecem 
    for i in range(linhas):
        for j in range(colunas):
            dicionario_de_letras[matriz[i][j]][0] += 1

def exibir_matriz(matriz, rodada): # mostro a matriz gerada
    print(f'======= RODADA {rodada} DE 10 =======')
    for letra in matriz:
        print(letra)

def calcular_pontuacao_rodada(dicionario_de_letras): # realizo o cálculo de ocorrencia de cada letra e sua pontuação de acordo com sua frequência com bsae na tabela de pontos, sem considerar o # (ele é o multiplicador de pontos)
    lista_de_pontos_rodada = []
    for chave in dicionario_de_letras: 
        ocorrencia = dicionario_de_letras[chave][0]

        if chave == '#':
            break
        elif ocorrencia >= 7:
            pontuacao = ocorrencia * dicionario_de_letras[chave][3]
        elif ocorrencia == 6:
            pontuacao = ocorrencia * dicionario_de_letras[chave][2]
        elif ocorrencia == 5:
            pontuacao = ocorrencia * dicionario_de_letras[chave][1]
        else:
            pontuacao = 0
        lista_de_pontos_rodada.append(pontuacao)

    if dicionario_de_letras['#'][0] > 0:
        multiplicador = dicionario_de_letras['#'][1] * dicionario_de_letras['#'][0]
    else:
        multiplicador = 1

    total_pontos_rodada = sum(lista_de_pontos_rodada) * multiplicador
    return total_pontos_rodada

def aguardar_proxima_rodada(): #string vazia retorna falso em python
    nova_rodada = input('Pressione [Enter] para a proxima rodada: ')
    while nova_rodada:
        nova_rodada = input('Pressione [Enter] para a proxima rodada: ')