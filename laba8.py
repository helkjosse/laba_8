import random
import logging

# Настройка логгинга
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создать файл лога с utf-8 кодировкой
file_handler = logging.FileHandler("log.log", encoding='utf-8')

# Создать форматтер, отображающий дату, время, имя регистратора, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавить обработчик к логгеру
logger.addHandler(file_handler)

def main():
    # Попросите пользователя ввести количество бочонков
    n = int(input("Введите количество бочонков: "))

    # Сформировать список чисел от 1 до N
    numbers = list(range(1, n + 1))

    # Перемешать список номеров
    random.shuffle(numbers)

    # Вытаскивать бочонки по одному
    for number in numbers:
        print(number)
        logger.info(f"Бочонок номер {number} вытащен")
        logger.info(f"Текущий лог вытащенных бочонков: {numbers[:numbers.index(number)+1]}")

if __name__ == "__main__":
    main()
