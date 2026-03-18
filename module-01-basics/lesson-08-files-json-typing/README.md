# Урок 1.8: Файлы, JSON, структура проекта и typing

Чтобы писать “как разработчик”, а не “как автор одного скрипта”, нужно уметь:
- сохранять данные в файлы;
- читать/писать JSON (конфиги, результаты);
- держать проект в понятной структуре;
- использовать type hints как “пояснения для себя, IDE и AI”.

## 🎯 Цели урока

- Чтение/запись файлов (UTF‑8)
- JSON: `json.load` / `json.dump` (+ `ensure_ascii=False`, `indent=2`)
- `pathlib.Path` для путей (без “склеивания строк”)
- Минимальная структура проекта: `src/`, `tests/`
- Базовые type hints: `list[int]`, `dict[str, str]`, `str | None`

## 📖 Теория и примеры

### 1) Читать/писать текст

```python
from pathlib import Path

path = Path("notes.txt")
path.write_text("Привет!\n", encoding="utf-8")
text = path.read_text(encoding="utf-8")
print(text)
```

### 2) Читать/писать JSON

```python
import json
from pathlib import Path

config_path = Path("config.json")
config = {"host": "127.0.0.1", "port": 8000}
config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")

loaded = json.loads(config_path.read_text(encoding="utf-8"))
print(loaded["host"], loaded["port"])
```

### 3) Type hints, которые реально помогают

```python
def build_url(host: str, port: int) -> str:
    return f"http://{host}:{port}"

tags: list[str] = ["python", "devops"]
limits: dict[str, int] = {"max_items": 100}
```

## 📁 Примеры кода

- [json_config.py](examples/json_config.py) — запись/чтение конфигурации

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

## 🏠 Домашнее задание

См. [homework.md](homework.md).

