import random
import math
from typing import List, Tuple
from src.models.item import Item
from src.algorithms.base import KnapsackSolver

class SimulatedAnnealingSolver(KnapsackSolver):
    def __init__(self, initial_temp: float = 1000.0, cooling_rate: float = 0.95, stopping_temp: float = 0.01):
        super().__init__("Simulated Annealing (Heuristic)")
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.stopping_temp = stopping_temp

    def _get_value_and_weight(self, solution: List[int], items: List[Item]) -> Tuple[int, int]:
        total_value = 0
        total_weight = 0
        for gene, item in zip(solution, items):
            if gene == 1:
                total_value += item.value
                total_weight += item.weight
        return total_value, total_weight

    def solve(self, items: List[Item], capacity: int) -> Tuple[int, List[Item]]:
        n = len(items)
        if n == 0: return 0, []

        # Rastgele geçerli bir başlangıç çözümü üret
        current_solution = [0] * n
        current_value, current_weight = self._get_value_and_weight(current_solution, items)

        best_solution = current_solution.copy()
        best_value = current_value

        temp = self.initial_temp

        while temp > self.stopping_temp:
            # Komşu çözüm üret (Rastgele bir biti değiştir)
            neighbor_idx = random.randint(0, n - 1)
            neighbor_solution = current_solution.copy()
            neighbor_solution[neighbor_idx] = 1 - neighbor_solution[neighbor_idx]

            n_value, n_weight = self._get_value_and_weight(neighbor_solution, items)

            # Eğer kapasite aşılmadıysa değerlendir
            if n_weight <= capacity:
                delta = n_value - current_value

                # Eğer daha iyiyse VEYA olasılık barajını geçiyorsa kabul et (Metropolis Kriteri)
                if delta > 0 or random.random() < math.exp(delta / temp):
                    current_solution = neighbor_solution
                    current_value = n_value

                    if current_value > best_value:
                        best_value = current_value
                        best_solution = current_solution.copy()

            # Sıcaklığı düşür
            temp *= self.cooling_rate

        selected_items = [items[i] for i in range(n) if best_solution[i] == 1]
        return best_value, selected_items