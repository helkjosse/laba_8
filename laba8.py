import random

def main():
    # Попросите пользователя ввести количество бочонков
    n = int(input("Введите количество бочонков: "))

    # Сформировать список чисел от 1 до N
    numbers = list(range(1, n + 1))

    # Перемешать список номеров
    random.shuffle(numbers)

    # Вытаскивать бочонки по одному
    log = []
    for number in numbers:
        log.append(number)
        print(number)

    # Выдать лог вытащенных бочонков
    print(f"Лог вытащенных бочонков: {log}")

if __name__ == "__main__":
    main()