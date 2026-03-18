from __future__ import annotations


def mean(a: float, b: float) -> float:
    """Return the arithmetic mean of two numbers."""
    return (a + b) / 2


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (ignoring spaces and case)."""
    normalized = "".join(ch.lower() for ch in s if not ch.isspace())
    return normalized == normalized[::-1]


def parse_int(s: str) -> int | None:
    """Parse int from string; return None when it can't be parsed."""
    try:
        return int(s.strip())
    except ValueError:
        return None


def main() -> None:
    print("mean:", mean(10, 20))
    print("is_palindrome:", is_palindrome("А роза упала на лапу Азора"))
    print("parse_int ok:", parse_int(" 42 "))
    print("parse_int bad:", parse_int("abc"))


if __name__ == "__main__":
    main()

