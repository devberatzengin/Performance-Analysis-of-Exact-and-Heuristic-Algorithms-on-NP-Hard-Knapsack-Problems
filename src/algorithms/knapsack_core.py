import random
import time
import math

def generate_knapsack_data(item_count, max_weight=50, max_value=100):
    # Creates random items for the problem: (value, weight)
    items = []

    for _ in range(item_count):
        value = random.randint(10, max_value)
        weight = random.randint(1, max_weight)
        items.append((value, weight))
    
    # Set capacity to 50% of total weight
    capacity = sum(w for v, w in items) // 2
    return items, capacity

def solve_knapsack_dp(items, capacity):
    # Solving with Dynamic Programming
    start_time = time.time()
    n = len(items)
    
    # Creating DP table (N+1 x Capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        v, w = items[i-1]
        for j in range(capacity + 1):
            if w <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else:
                dp[i][j] = dp[i-1][j]
    
    end_time = time.time()
    return dp[n][capacity], end_time - start_time

def solve_knapsack_ga(items, capacity, pop_size=50, generations=100):
    # Solving with Genetic Algorithm
    start_time = time.time()
    n = len(items)

    # 1. Initial Population (Creating random backpacks)
    # Each individual consists of 0s and 1s indicating whether items are taken.
    population = []
    for _ in range(pop_size):
        individual = [random.randint(0, 1) for _ in range(n)]
        population.append(individual)

    def get_fitness(individual):
        # Calculates the total value of the backpack, returns 0 if capacity is exceeded
        total_value = 0
        total_weight = 0
        for i in range(n):
            if individual[i] == 1:
                total_value += items[i][0]
                total_weight += items[i][1]
        if total_weight > capacity:
            return 0  # Exceeding capacity makes the backpack worthless
        return total_value

    # 2. Evolution Process
    for _ in range(generations):
        # Sort population according to fitness score
        population.sort(key=get_fitness, reverse=True)
        
        # Select some of the best ones (Elitism)
        new_population = population[:10]

        # Fill the population with new individuals
        while len(new_population) < pop_size:
            # Crossover: Select two good parents and mix them
            parent1 = random.choice(population[:20])
            parent2 = random.choice(population[:20])
            point = random.randint(1, n - 1)
            child = parent1[:point] + parent2[point:]

            # Mutation: Sometimes randomly change an item
            if random.random() < 0.1: # 10% probability of mutation
                idx = random.randint(0, n - 1)
                child[idx] = 1 - child[idx]
            
            new_population.append(child)
        
        population = new_population

    # Find the best result
    best_individual = max(population, key=get_fitness)
    best_value = get_fitness(best_individual)
    
    end_time = time.time()
    return best_value, end_time - start_time

def solve_knapsack_sa(items, capacity, temp=1000, cooling_rate=0.99, iterations=1000):
    # Solving with Simulated Annealing
    start_time = time.time()
    n = len(items)
    
    # 1. Initial Solution (Random backpack)
    def get_value_and_weight(solution):
        v, w = 0, 0
        for i in range(n):
            if solution[i] == 1:
                v += items[i][0]
                w += items[i][1]
        return (v, w) if w <= capacity else (0, w)

    current_sol = [random.randint(0, 1) for _ in range(n)]
    current_val, _ = get_value_and_weight(current_sol)
    
    best_sol = list(current_sol)
    best_val = current_val
    
    t = temp
    
    # 2. Annealing Process
    for _ in range(iterations):
        # Generate Neighbor Solution (Change a random bit)
        neighbor = list(current_sol)
        idx = random.randint(0, n - 1)
        neighbor[idx] = 1 - neighbor[idx]
        
        neighbor_val, _ = get_value_and_weight(neighbor)
        
        # Acceptance Criterion (Metropolis Algorithm)
        if neighbor_val > current_val:
            current_sol = neighbor
            current_val = neighbor_val
        else:
            # If it's worse, accept it with a certain probability
            diff = neighbor_val - current_val
            if math.exp(diff / t) > random.random():
                current_sol = neighbor
                current_val = neighbor_val
        
        # Update Best Solution
        if current_val > best_val:
            best_val = current_val
            best_sol = list(current_sol)
            
        # Cooling
        t *= cooling_rate
        if t < 0.01: break
            
    return best_val, time.time() - start_time