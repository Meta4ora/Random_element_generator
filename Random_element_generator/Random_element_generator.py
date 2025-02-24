import random

def generate_random_numbers(count):
    # Генерирует список случайных чисел в диапазоне от 5 до 1600.
    return [random.randint(5, 16 * 100) for _ in range(count)]

if __name__ == "__main__":
    number_of_elements = 16 + 10  # 26 элементов (10 + 16)
    random_numbers = generate_random_numbers(number_of_elements)
    
    # Вывод сгенерированных чисел
    print("Сгенерированные случайные числа:")
    for i, number in enumerate(random_numbers, start=1):
        print(f"Число {i}: {number}")
