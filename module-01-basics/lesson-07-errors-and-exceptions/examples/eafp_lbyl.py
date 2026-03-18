"""
Пример: LBYL vs EAFP на словаре.
"""


def lbyl(data: dict) -> str | None:
    if "name" in data:
        return data["name"]
    return None


def eafp(data: dict) -> str | None:
    try:
        return data["name"]
    except KeyError:
        return None


def main() -> None:
    samples = [{"name": "VibeOps"}, {}, {"name": 123}]
    for s in samples:
        print("data:", s, "LBYL:", lbyl(s), "EAFP:", eafp(s))


if __name__ == "__main__":
    main()

