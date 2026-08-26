from funcoes import(
    aguardar_proxima_rodada, 
    calcular_pontuacao_rodada,
    contar_ocorrencias, 
    exibir_matriz,
    gerar_matriz, 
    obter_tabela_letras
)

def main():
    linhas = 5
    colunas = 6
    rodadas = 1
    lista_de_pontos_final = []

    while rodadas <= 10:
        dicionario_de_letras = obter_tabela_letras()
        lista_de_letras = list(dicionario_de_letras.keys())

        matriz = gerar_matriz(linhas, colunas, lista_de_letras)
        contar_ocorrencias(matriz, dicionario_de_letras, linhas, colunas)
        exibir_matriz(matriz, rodadas)

        total_pontos_rodada = calcular_pontuacao_rodada(dicionario_de_letras)
        print(f'Pontuação da rodada: {total_pontos_rodada:.2f}')
        lista_de_pontos_final.append(total_pontos_rodada)

        aguardar_proxima_rodada()
        rodadas += 1 # mudando as rodadas
        print()

    pontuacao_total = sum(lista_de_pontos_final)
    print(f'\nPontuação final: {pontuacao_total:.2f}')

if __name__ == '__main__':
    main()