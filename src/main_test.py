from src.utils.data_generator import generate_knapsack_data
from src.utils.plotter import plot_performance
from src.algorithms.dynamic_programming import DynamicProgrammingSolver
from src.algorithms.genetic import GeneticAlgorithmSolver
from src.algorithms.simulated_annealing import SimulatedAnnealingSolver
import os

def main():
    # Çıktı klasörü yoksa oluştur
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    # Çözücüleri tanımla
    solvers = [
        DynamicProgrammingSolver(),
        GeneticAlgorithmSolver(pop_size=40, generations=100),
        SimulatedAnnealingSolver(initial_temp=500, cooling_rate=0.98)
    ]

    # Test edilecek veri büyüklükleri (N değerleri)
    # NOT: DP, N=100'den sonra şişebilir, hocaya göstermek için ideal aralıklar
    item_sizes = [10, 20, 30, 50, 100]
    
    # Grafik verisi toplama sözlüğü
    performance_results = {solver.name: {} for solver in solvers}

    print("=== Knapsack Performans Analizi Başlatılıyor ===\n")

    for size in item_sizes:
        print(f"--- Test Ölçümü Yapılıyor | Eleman Sayısı (N): {size} ---")
        
        # Test verisini üret ve kapasiteyi ayarla
        items = generate_knapsack_data(num_items=size)
        total_weight = sum(item.weight for item in items)
        capacity = int(total_weight * 0.5) # Toplam ağırlığın yarısı kapasite olsun

        for solver in solvers:
            # Zaman ölçümlü çözücü fonksiyonumuzu çağırıyoruz
            max_val, selected, exec_time = solver.solve_with_timer(items, capacity)
            
            # Sonuçları kaydet
            performance_results[solver.name][size] = exec_time
            print(f" > {solver.name:35} | Süre: {exec_time:.6f} sn | En İyi Kazanç: {max_val}")
        print()

    # Performans Grafiğini Çizdir ve Kaydet
    print("[+] Analiz bitti. Grafikler 'outputs/performance_chart.png' adresine kaydediliyor...")
    plot_performance(performance_results)
    print("[+] İşlem tamamlandı!")

if __name__ == "__main__":
    main()