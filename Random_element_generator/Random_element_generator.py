import random

def generate_random_numbers(count):
    #Генерирует список случайных чисел в диапазоне от 5 до 1600. В параметрах передаем число сгенерированных чисел
    numbers = [random.randint(5, 16 * 100) for x in range(count)]
    return numbers

if __name__ == "__main__":
    number_of_elements = 16 + 10  # 26 элементов (10+16)
    random_numbers = generate_random_numbers(number_of_elements)
    
    # Вывод сгенерированных чисел
    print("Сгенерированные случайные числа:")
    for number in random_numbers:
        print(number)

