import random
from collections import Counter

# 1. Definir a lista de strings
participantes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# 2. Definir a quantidade de simulações
total_simulacoes = 10

# 3. Executar o sorteio aleatório 100 vezes
resultados = [random.choice(participantes) for _ in range(total_simulacoes)]

# 4. Contar quantas vezes cada string foi sorteada
contagem = Counter(resultados)

# 5. Exibir as chances calculadas
print(f"--- Resultado de {total_simulacoes} Simulações ---")
for string in participantes:
    # Vezes sorteada dividido por 100 simulações multiplicado por 100 resulta no próprio contador
    frequencia_porcentagem = (contagem[string] / total_simulacoes) * 100
    
    print(f"String: {string:<11} | Sorteada: {contagem[string]:>2} vezes | Chance Real: {frequencia_porcentagem:.3f}%")

# Chance teórica matemática
chance_teorica = (1 / len(participantes)) * 100
print(f"\n* A chance teórica exata para cada uma era de: {chance_teorica:.3f}%")
