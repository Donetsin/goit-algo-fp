import random
import matplotlib.pyplot as plt

# Кількість імітацій
num_simulations = 100000

# Ініціалізація лічильників для кожної можливої суми
sum_counts = {i: 0 for i in range(2, 13)}

# Самостійно написаний метод Монте-Карло
def monte_carlo_simulation(num_simulations):
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sum_counts[total] += 1

# Виконання симуляції
monte_carlo_simulation(num_simulations)

# Обчислення ймовірностей за методом Монте-Карло
probabilities_monte_carlo = {sum: count / num_simulations for sum, count in sum_counts.items()}

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36
}

# Виведення результатів
print("Ймовірності сум при киданні двох кубиків:")
print("Сума\tМонте-Карло\tАналітичні")
for sum in range(2, 13):
    print(f"{sum}\t{probabilities_monte_carlo[sum]:.4f}\t\t{analytical_probabilities[sum]:.4f}")

# Графік ймовірностей
plt.bar(probabilities_monte_carlo.keys(), probabilities_monte_carlo.values(), color='blue', alpha=0.5, label='Монте-Карло')
plt.bar(analytical_probabilities.keys(), analytical_probabilities.values(), color='red', alpha=0.5, label='Аналітичні')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.xticks(range(2, 13))
plt.legend()
plt.show()