from __future__ import annotations


def find_by_category(items: list[dict[str, object]], category: str) -> list[dict[str, object]]:
    category = category.strip().lower()
    if not category:
        return []

    result: list[dict[str, object]] = []
    for item in items:
        item_category = str(item.get("category", "")).strip().lower()
        if item_category == category:
            result.append(item)
    return result


def unique_categories(items: list[dict[str, object]]) -> set[str]:
    categories: set[str] = set()
    for item in items:
        category = str(item.get("category", "")).strip()
        if category:
            categories.add(category)
    return categories


def main() -> None:
    products = [
        {"name": "Молоток", "price": 350, "category": "tools"},
        {"name": "Отвёртка", "price": 200, "category": "tools"},
        {"name": "Чистый код", "price": 900, "category": "books"},
        {"name": "Гвозди", "price": 120, "category": "tools"},
    ]

    print("Категории:", sorted(unique_categories(products)))
    print("Tools:", find_by_category(products, "tools"))
    print("Books:", find_by_category(products, "books"))


if __name__ == "__main__":
    main()

