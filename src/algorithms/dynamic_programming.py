from typing import List, Tuple
from src.models.item import Item
from src.algorithms.base import KnapsackSolver

class DynamicProgrammingSolver(KnapsackSolver):
    def __init__(self):
        super().__init__("Dynamic Programming (Exact)")

    def solve(self, items: List[Item], capacity: int) -> Tuple[int, List[Item]]:
        n = len(items)
        # Bellek optimizasyonlu DP tablosu
        dp = [0] * (capacity + 1)
        # Hangi elemanların seçildiğini geriye doğru bulmak için takip matrisi
        keep = [[False] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            item = items[i - 1]
            # Kapasiteyi geriye doğru tarıyoruz (Aynı elemanı tekrar kullanmamak için)
            for w in range(capacity, -1, -1):
                if item.weight <= w:
                    if dp[w - item.weight] + item.value > dp[w]:
                        dp[w] = dp[w - item.weight] + item.value
                        keep[i][w] = True

        # Seçilen elemanları geriye doğru bulma (Backtracking)
        selected_items = []
        w = capacity
        for i in range(n, 0, -1):
            if keep[i][w]:
                item = items[i - 1]
                selected_items.append(item)
                w -= item.weight

        return dp[capacity], selected_items