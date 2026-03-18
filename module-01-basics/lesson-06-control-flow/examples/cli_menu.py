"""
Пример: простое CLI-меню на input() + while.
"""


def main() -> None:
    while True:
        cmd = input("Команда (hello/exit): ").strip().lower()
        if cmd == "exit":
            print("Пока!")
            break
        if cmd == "hello":
            name = input("Имя: ").strip()
            if not name:
                print("Имя не может быть пустым")
                continue
            print(f"Привет, {name}!")
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()

