import random
from typing import List
from src.models.item import Item

def generate_knapsack_data(num_items: int, min_val: int = 10, max_val: int = 100, min_weight: int = 5, max_weight: int = 50) -> List[Item]:
    """Performans testleri için rastgele Item listesi üretir."""
    items = []
    for i in range(1, num_items + 1):
        value = random.randint(min_val, max_val)
        weight = random.randint(min_weight, max_weight)
        items.append(Item(id=i, value=value, weight=weight))
    return items