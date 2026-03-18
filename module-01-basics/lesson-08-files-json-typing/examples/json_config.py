"""
Пример: запись/чтение JSON конфигурации.
"""

import json
from pathlib import Path


def write_config(path: Path, config: dict) -> None:
    path.write_text(
        json.dumps(config, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def read_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    path = Path("config.json")
    write_config(path, {"host": "127.0.0.1", "port": 8000})
    cfg = read_config(path)
    print(cfg["host"], cfg["port"])


if __name__ == "__main__":
    main()

