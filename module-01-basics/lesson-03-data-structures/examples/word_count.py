from __future__ import annotations


def normalize_word(word: str) -> str:
    return word.strip().lower().strip(".,!?;:()[]\"'")


def word_frequencies(text: str) -> dict[str, int]:
    freqs: dict[str, int] = {}
    for raw in text.split():
        w = normalize_word(raw)
        if not w:
            continue
        freqs[w] = freqs.get(w, 0) + 1
    return freqs


def top_n(freqs: dict[str, int], n: int) -> list[tuple[str, int]]:
    return sorted(freqs.items(), key=lambda kv: kv[1], reverse=True)[:n]


def main() -> None:
    text = "AI пишет код. AI ошибается. Код нужно проверять, а не копировать."
    freqs = word_frequencies(text)
    print("Топ-5:", top_n(freqs, 5))


if __name__ == "__main__":
    main()

