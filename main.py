import random

pontuacao_total = 0
lista_de_pontos_final = []

for l in range(10):
    linhas = 5
    colunas = 6
    matriz = []

    dicionario_de_letras = {
        'I': [0, 0.25, 0.75, 2],
        'H': [0, 0.4, 0.9, 4],
        'G': [0, 0.5, 1, 5],
        'F': [0, 0.8, 1.2, 8],
        'E': [0, 1, 1.5, 10],
        'D': [0, 1.5, 2, 12],
        'C': [0, 2, 5, 15],
        'B': [0, 2.5, 10, 25],
        'A': [0, 10, 25, 50 ],
    }
    lista_de_letras = list(dicionario_de_letras.keys())

    lista_de_pontos_rodada = []

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

    # mostro a matriz gerada
    for i in matriz:
        print(i)

    # realizando o cálculo de ocorrencia de cada letra e sua pontuação de acordo com a tabela de pontos
    for chave in dicionario_de_letras: 
        # MOSTRANDO QUANTAS VEZES AS LETRAS APARECEM   
        #print(f'A letra {chave} aparece {dicionario_de_letras[chave][0]} vezes')

        ocorrencia = dicionario_de_letras[chave][0]
        if ocorrencia >= 7:
            pontuacao = ocorrencia * dicionario_de_letras[chave][3]
        elif ocorrencia == 6:
            pontuacao = ocorrencia * dicionario_de_letras[chave][2]
        elif ocorrencia == 5:
            pontuacao = ocorrencia * dicionario_de_letras[chave][1]
        else:
            pontuacao = 0
        lista_de_pontos_rodada.append(pontuacao)

    total_pontos_rodada = 0
    for pontos in lista_de_pontos_rodada:
        total_pontos_rodada += pontos

    print(f'Pontuação da rodada: {total_pontos_rodada}\n')

    lista_de_pontos_final.append(total_pontos_rodada)

for i in lista_de_pontos_final:
    pontuacao_total += i

print(f'\nPontuação final: {pontuacao_total}')