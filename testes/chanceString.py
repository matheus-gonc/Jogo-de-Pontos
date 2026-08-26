import random
from collections import Counter

strings = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '#']
total = 10000000

# random.choices com 'k=' faz o sorteio em massa muito mais rápido e sem gastar memória extra
contagem = Counter(random.choices(strings, k=total))

print(f"--- Resultado de {total} Simulações ---")
for item, qtd in contagem.items():
    pct = (qtd / total) * 100
    print(f"String: {item:<2} | Sorteada: {qtd:>8} vezes | Chance Real: {pct:.3f}%")

print(f"\n* Chance teórica exata: {100 / len(strings):.3f}%")