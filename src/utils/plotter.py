import matplotlib.pyplot as plt
from typing import List, Dict

def plot_performance(results: Dict[str, Dict[int, float]], output_path: str = "outputs/performance_chart.png"):
    """
    Algoritmaların eleman sayısına (N) göre harcadığı süreleri çizgi grafik olarak kaydeder.
    results formatı: {'Algo Name': {10: 0.001, 50: 0.02, 100: 0.5}}
    """
    plt.figure(figsize=(10, 6))

    for algo_name, data in results.items():
        sizes = sorted(data.keys())
        times = [data[size] for size in sizes]
        plt.plot(sizes, times, marker='o', label=algo_name, linewidth=2)

    plt.title("Knapsack Algorithms Performance Analysis", fontsize=14, fontweight='bold')
    plt.xlabel("Number of Items (N)", fontsize=12)
    plt.ylabel("Execution Time (Seconds)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=10)
    
    # Grafiği kaydet
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()