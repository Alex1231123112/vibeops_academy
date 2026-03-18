# Шпаргалка: Зависимости (урок 2.5)

## venv (создать и активировать)

| Действие | Команда |
|---|---|
| Создать venv | `python -m venv .venv` |
| Активировать (Windows) | `.venv\\Scripts\\activate` |
| Активировать (macOS/Linux) | `source .venv/bin/activate` |
| Выйти из venv | `deactivate` |

## pip (минимум)

| Действие | Команда |
|---|---|
| Установить пакет | `pip install requests` |
| Установить из requirements | `pip install -r requirements.txt` |
| Сохранить зависимости | `pip freeze > requirements.txt` |
| Посмотреть установленные | `pip list` |

## Быстрая проверка “я в venv?”

- В терминале виден префикс `(.venv)`  
- `where python` (Windows) / `which python` (macOS/Linux) указывает на `.venv/...`

