import numpy as np

criteria = [
    "Город",
    "Рейтинг",
    "Направление",
    "Преподаватели",
    "Студенческая жизнь",
    "Общежитие"
]

alternatives = ["МАИ", "МИРЭА", "МФТИ"]

def normalize_matrix(matrix):
    col_sum = np.sum(matrix, axis=0)
    return matrix / col_sum

def calculate_weights(matrix):
    normalized = normalize_matrix(matrix)
    return np.mean(normalized, axis=1)

def input_matrix(names):
    n = len(names)
    matrix = np.ones((n, n))
    print("\nПопарные сравнения:")
    for i in range(n):
        for j in range(i+1, n):
            print(f"\nЧто важнее: {names[i]} или {names[j]}?")
            val = float(input(f"Введите значение ({names[i]} к {names[j]}): "))
            matrix[i][j] = val
            matrix[j][i] = 1 / val
    return matrix

def main():

    print("\nСРАВНЕНИЕ КРИТЕРИЕВ")
    criteria_matrix = input_matrix(criteria)
    criteria_weights = calculate_weights(criteria_matrix)

    print("\nВеса критериев:")
    for i, c in enumerate(criteria):
        print(f"{c}: {criteria_weights[i]:.4f}")

    alt_weights = []

    for i, criterion in enumerate(criteria):
        print(f"\nСРАВНЕНИЕ УНИВЕРСИТЕТОВ ПО КРИТЕРИЮ: {criterion}")
        matrix = input_matrix(alternatives)
        weights = calculate_weights(matrix)
        alt_weights.append(weights)

    alt_weights = np.array(alt_weights).T

    print("\nМатрица весов альтернатив:")
    print(alt_weights)

    final_scores = np.dot(alt_weights, criteria_weights)

    print("\nИТОГОВЫЕ ОЦЕНКИ:")
    for i, alt in enumerate(alternatives):
        print(f"{alt}: {final_scores[i]:.4f}")

    best = np.argmax(final_scores)
    print(f"\nЛучший выбор: {alternatives[best]}")

if __name__ == "__main__":
    main()