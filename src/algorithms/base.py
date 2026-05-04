from abc import ABC, abstractmethod
from typing import List, Tuple
import time
from src.models.item import Item

class KnapsackSolver(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def solve(self, items: List[Item], capacity: int) -> Tuple[int, List[Item]]:
        """
        Her algoritma bu metodu ezmek zorundadır.
        Geriye: (Maksimum Kazanç, Seçilen Elemanların Listesi) döner.
        """
        pass

    def solve_with_timer(self, items: List[Item], capacity: int) -> Tuple[int, List[Item], float]:
        """Algoritmaların çalışma süresini hassas ölçen ortak metot."""
        start_time = time.perf_counter()
        max_value, selected_items = self.solve(items, capacity)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        return max_value, selected_items, execution_time