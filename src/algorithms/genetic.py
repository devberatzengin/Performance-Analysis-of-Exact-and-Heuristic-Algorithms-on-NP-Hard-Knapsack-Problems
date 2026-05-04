import random
from typing import List, Tuple
from src.models.item import Item
from src.algorithms.base import KnapsackSolver

class GeneticAlgorithmSolver(KnapsackSolver):
    def __init__(self, pop_size: int = 50, generations: int = 100, mutation_rate: float = 0.05):
        super().__init__("Genetic Algorithm (Heuristic)")
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def _calculate_fitness(self, chromosome: List[int], items: List[Item], capacity: int) -> int:
        total_value = 0
        total_weight = 0
        for gene, item in zip(chromosome, items):
            if gene == 1:
                total_value += item.value
                total_weight += item.weight
        # Kapasite aşımı varsa cezalandırma (Penalty) uyguluyoruz
        return total_value if total_weight <= capacity else 0

    def solve(self, items: List[Item], capacity: int) -> Tuple[int, List[Item]]:
        n = len(items)
        if n == 0: return 0, []

        # 1. Başlangıç Popülasyonu Oluşturma
        population = [[random.randint(0, 1) for _ in range(n)] for _ in range(self.pop_size)]

        best_chromosome = population[0]
        best_fitness = self._calculate_fitness(best_chromosome, items, capacity)

        for _ in range(self.generations):
            # Fitness değerlerini hesapla
            fitness_scores = [self._calculate_fitness(chrom, items, capacity) for chrom in population]
            
            # En iyiyi güncelle
            for chrom, score in zip(population, fitness_scores):
                if score > best_fitness:
                    best_fitness = score
                    best_chromosome = chrom

            # 2. Seçilim (Roulette Wheel veya Tournament) - Basitlik için Turnuva Seçimi
            next_population = []
            for _ in range(self.pop_size):
                i1, i2 = random.sample(range(self.pop_size), 2)
                winner = population[i1] if fitness_scores[i1] > fitness_scores[i2] else population[i2]
                next_population.append(winner.copy())

            # 3. Çaprazlama (Crossover) - Tek Noktalı Çaprazlama
            for i in range(0, self.pop_size, 2):
                if i + 1 < self.pop_size and random.random() < 0.8:
                    crossover_point = random.randint(1, n - 1)
                    next_population[i][crossover_point:], next_population[i+1][crossover_point:] = \
                        next_population[i+1][crossover_point:], next_population[i][crossover_point:]

            # 4. Mutasyon
            for chrom in next_population:
                for j in range(n):
                    if random.random() < self.mutation_rate:
                        chrom[j] = 1 - chrom[j] # Biti tersine çevir (0->1, 1->0)

            population = next_population

        # Kromozom diziliminden Item nesnelerine geri dönüştürme
        selected_items = [items[i] for i in range(n) if best_chromosome[i] == 1]
        return best_fitness, selected_items