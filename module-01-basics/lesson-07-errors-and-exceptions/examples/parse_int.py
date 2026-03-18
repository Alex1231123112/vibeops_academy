"""
Пример: устойчивый ввод целого числа.
"""


def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Нужно целое число. Пример: 42")


def main() -> None:
    x = read_int("Введите число: ")
    print("Ок:", x)


if __name__ == "__main__":
    main()

