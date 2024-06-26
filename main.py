#Пояснение:
# Функция filter_short_strings(strings):

# Создает пустой массив result для хранения строк, длина которых меньше или равна 3 символам.
# Проходит по каждому элементу в исходном массиве strings и проверяет длину строки.
# Если длина строки меньше или равна 3, добавляет эту строку в result.
# Функция main():

# Задает исходный массив строк. Здесь массив задается вручную, но можно раскомментировать строку с input(), чтобы вводить строки с клавиатуры.
# Вызывает функцию filter_short_strings() для фильтрации строк.
# Выводит исходный и отфильтрованный массивы на экран.
# Примеры работы программы:
# Для исходного массива ["Hello", "2", "world", ":-)"] программа выведет отфильтрованный массив ["2", ":-)"].
# Для исходного массива ["1234", "1567", "-2", "computer science"] программа выведет отфильтрованный массив ["-2"].
# Для исходного массива ["Russia", "Denmark", "Kazan"] программа выведет пустой массив [], так как нет строк длиной меньше или равной 3 символам.
# Этот подход решает задачу без использования сложных коллекций, только с помощью базовых массивов и циклов.



def filter_short_strings(strings):
    # Создаем новый массив для строк, длина которых <= 3
    result = []
    for string in strings:
        if len(string) <= 3:
            result.append(string)
    return result

def main():
    # Исходный массив можно задать вручную или ввести с клавиатуры
    # Пример с заданным массивом:
    initial_array = ["Hello", "2", "world", ":-)"]
    # Пример с вводом массива с клавиатуры:
    # initial_array = input("Введите строки через пробел: ").split()
    
    # Фильтрация строк
    filtered_array = filter_short_strings(initial_array)
    
    # Вывод результата
    print("Исходный массив:", initial_array)
    print("Отфильтрованный массив:", filtered_array)

if __name__ == "__main__":
    main()
