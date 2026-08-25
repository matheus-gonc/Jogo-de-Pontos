import random

pontuacao_total = 0
lista_de_pontos_final = []

linhas = 5
colunas = 6

rodadas = 1
while rodadas <= 10:
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
        'A': [0, 10, 25, 50],
        '#': [0, 2]
    }
    lista_de_letras = list(dicionario_de_letras.keys())

    lista_de_pontos_rodada = []

    # gera a matriz e colocar letras aleatórias nela
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            numero = random.choice(lista_de_letras)
            linha.append(numero)
        matriz.append(linha)

    # contando a quantidade de vezes que as letras aparecem 
    for i in range(linhas):
        for j in range(colunas):
            dicionario_de_letras[matriz[i][j]][0] += 1

    # mostro a matriz gerada
    print(f'======= RODADA {rodadas} DE 10 =======')
    for letra in matriz:
        print(letra)

    # realizo o cálculo de ocorrencia de cada letra e sua pontuação de acordo com sua frequência com bsae na tabela de pontos, sem considerar o # (ele é o multiplicador de pontos)
    for chave in dicionario_de_letras: 
        # MOSTRANDO QUANTAS VEZES AS LETRAS APARECEM
        #print(f'A letra {chave} aparece {dicionario_de_letras[chave][0]} vezes')

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


    total_pontos_rodada = 0
    for pontos in lista_de_pontos_rodada:
        total_pontos_rodada += pontos
    total_pontos_rodada = total_pontos_rodada * multiplicador
        

    print(f'Pontuação da rodada: {total_pontos_rodada:.2f}')

    lista_de_pontos_final.append(total_pontos_rodada)

    nova_rodada = input('Pressione [Enter] para a proxima rodada: ') #string vazia retorna falso em python
    if not nova_rodada:
        rodadas += 1 # mudando as rodadas
    else:
        while nova_rodada:
            nova_rodada = input('Pressione [Enter] para a proxima rodada: ')
            if not nova_rodada:
                rodadas += 1

    print()

for i in lista_de_pontos_final:
    pontuacao_total += i

print(f'\nPontuação final: {pontuacao_total:.2f}')