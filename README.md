# Performance Analysis of Exact and Heuristic Algorithms on NP-Hard Knapsack Problems

This project provides a comprehensive performance and comparative analysis of exact and heuristic algorithmic approaches for solving the **NP-Hard 0/1 Knapsack Problem**. 

The implementation evaluates and compares the execution efficiency and solution quality of **Dynamic Programming (Exact)**, **Genetic Algorithms (Heuristic)**, and **Simulated Annealing (Heuristic)** across various problem dimensions ($N$).

## 📂 Project Structure

```text
knapsack-performance-analysis/
│
├── src/
│   ├── main_test.py            # Main entry point for benchmarks
│   ├── models/                 # Object-oriented data models
│   │   └── item.py
│   ├── algorithms/             # Algorithmic implementations
│   │   ├── base.py             # Abstract base class with high-precision timers
│   │   ├── dynamic_programming.py
│   │   ├── genetic.py
│   │   └── simulated_annealing.py
│   └── utils/                  # Analytical helpers
│       ├── data_generator.py
│       └── plotter.py
│
├── requirements.txt            # System dependencies
└── .gitignore