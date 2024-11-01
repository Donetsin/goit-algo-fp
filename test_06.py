items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості (у порядку спадання)
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_calories

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    item_list = list(items.items())

    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_name, item_details = item_list[i - 1]
            if item_details['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_details['cost']] + item_details['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, item_details = item_list[i - 1]
            selected_items.append(item_name)
            w -= item_details['cost']

    total_calories = dp[n][budget]
    return selected_items, total_calories

# Приклад використання
budget = 100

# Жадібний алгоритм
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print(f"Вибрані страви: {selected_items_greedy}")
print(f"Загальна калорійність: {total_calories_greedy}")

# Алгоритм динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print(f"Вибрані страви: {selected_items_dp}")
print(f"Загальна калорійність: {total_calories_dp}")