from __future__ import annotations


class Task:
    def __init__(self, title: str) -> None:
        title = title.strip()
        if not title:
            raise ValueError("title не может быть пустым")
        self.title = title
        self.done = False

    def toggle(self) -> None:
        self.done = not self.done

    def __str__(self) -> str:
        mark = "x" if self.done else " "
        return f"[{mark}] {self.title}"


def main() -> None:
    task = Task("Прочитать урок 1.4")
    print(task)
    task.toggle()
    print(task)


if __name__ == "__main__":
    main()

