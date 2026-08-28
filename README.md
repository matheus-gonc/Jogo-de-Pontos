# 🎰 Jogo de Matrizes e Pontuação em Python

## 🎯 Objetivo do Projeto
Este projeto foi desenvolvido com o objetivo principal de reforçar a minha lógica de programação através da aplicação prática e manipulação de diferentes estruturas de dados. O arquivo `funcoes.py` guarda as configurações e regras, enquanto o `main.py` executa o programa.

## ⚙️ Como o Código Funciona
O algoritmo simula um jogo de sorteio baseado em grade (semelhante a uma *slot machine*), que ocorre ao longo de **10 rodadas**. 
Em cada rodada, é gerada uma matriz de dimensão 5x6 preenchida com caracteres aleatórios (letras de 'A' a 'I' e o símbolo especial '#'). O sistema então contabiliza a frequência de cada caractere na matriz gerada e calcula a pontuação da rodada com base em regras de multiplicadores de ocorrência.

### O fluxo principal consiste em:
1. **Geração Aleatória de Matrizes:** Geração de uma matriz 5x6 a cada rodada com distribuição uniforme das letras.
2. **Sistema de Contagem e Frequência:** Varredura da matriz para identificar o número exato de ocorrências de cada item, em seguida a frequência é guardada no dicionário.
3. **Cálculo Dinâmico de Pontuação:** Cálculo da pontuação baseado no número de repetições (mínimo de 5 para pontuar) e nos pesos de cada letra.
4. **Multiplicador Especial (Curinga):** O símbolo `#` não tem valor próprio, mas atua como um multiplicador global para os pontos da rodada.
5. **Controle de Fluxo (Pausas):** Após o cálculo das pontuações, o sistema aguarda a interação do usuário (`[Enter]`) para avançar entre as rodadas, facilitando a visualização dos resultados parciais, e posteriormente a pontuação final.

## 📊 Tabela de Pontuação
Para que uma letra gere pontos, ela deve aparecer **pelo menos 5 vezes** na matriz da rodada. O valor final da letra é calculado multiplicando o número de ocorrências pelo multiplicador correspondente na tabela abaixo:

| Símbolo | 5 Ocorrências (x) | 6 Ocorrências (x) | 7 ou mais Ocorrências (x) |
|:---:|:---:|:---:|:---:|
| **I** | 0.25 | 0.75 | 2.00 |
| **H** | 0.40 | 0.90 | 4.00 |
| **G** | 0.50 | 1.00 | 5.00 |
| **F** | 0.80 | 1.20 | 8.00 |
| **E** | 1.00 | 1.50 | 10.00 |
| **D** | 1.50 | 2.00 | 12.00 |
| **C** | 2.00 | 5.00 | 15.00 |
| **B** | 2.50 | 10.00 | 25.00 |
| **A** | 10.00 | 25.00 | 50.00 |

**⭐ Multiplicador Global (`#`):**
Se o símbolo `#` aparecer na matriz, ele multiplica a soma total dos pontos da rodada. O valor do multiplicador é igual a `2 * (quantidade de '#')`. Se nenhum `#` for sorteado, o multiplicador da rodada será `1` (pontuação normal).

## 🗂️ Estruturas de Dados Utilizadas
O aprimoramento da lógica de programação neste projeto se deu fortemente pelo uso combinado das seguintes estruturas de dados nativas do Python:
* **Dicionários (`dict`):** Utilizados como tabela de *hash* em `obter_tabela_letras()` para mapear os caracteres (chaves) às suas respectivas regras de pontuação (lista de valores contendo contagem e multiplicadores).
* **Matrizes (Listas de Listas):** Utilizadas para representar bidimensionalmente a grade do jogo (linhas e colunas), construídas através de laços de repetição (loops) aninhados.
* **Listas (`list`):** Empregadas em múltiplas frentes:
  * Como valores do dicionário para armazenar as propriedades das letras.
  * Para iterar sobre as chaves (letras disponíveis) via `list(dicionario_de_letras.keys())`.
  * Para armazenar o histórico de pontos de cada rodada (`lista_de_pontos_rodada` e `lista_de_pontos_final`) e calcular os somatórios com a função `sum()`.

## 💻 Como Executar

**Pré-requisitos:**
* Ter o [Python 3.x](https://www.python.org/downloads/) instalado na máquina.

**Passo a passo:**
1. Clone este repositório ou faça o download dos arquivos.
2. Certifique-se de que os arquivos `main.py` e `funcoes.py` estão no mesmo diretório.
3. Abra o terminal e navegue até a pasta onde os arquivos estão localizados.
4. Execute o arquivo principal com o comando:
```bash
python main.py
```
5. Acompanhe a matriz sendo gerada no terminal e pressione `[Enter]` para avançar as rodadas!

## 👤 Autor
Desenvolvido por **Matheus Gonçalves** como um projeto de estudo de modelagem e lógica de programação em Python.