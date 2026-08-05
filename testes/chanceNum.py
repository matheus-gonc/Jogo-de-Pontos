import random
from collections import Counter

# Gera 100 mil números entre 1 e 5
simulacao = [random.randint(1, 5) for _ in range(100000)]
contagem = Counter(simulacao)

# Exibe a porcentagem real de cada um
for numero, qtd in sorted(contagem.items()):
    porcentagem = (qtd / 100000) * 100
    print(f"Número {numero}: {porcentagem:.3f}% de chance")
