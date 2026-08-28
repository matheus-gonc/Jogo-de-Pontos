import random
from collections import Counter

strings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '#']
simulacoes = 10000000

contagem = Counter(random.choices(strings, k=simulacoes))

print(f"--- Resultado de {simulacoes} Simulações ---")
for item, qtd in contagem.items():
    pct = (qtd / simulacoes) * 100
    print(f"String: {item:<2} | Sorteada: {qtd:>8} vezes | Chance Real: {pct:.3f}%")

print(f"\n* Chance teórica exata: {100 / len(strings):.3f}%")