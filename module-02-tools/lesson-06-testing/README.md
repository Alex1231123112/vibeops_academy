# Урок 2.6: Тестирование (pytest) и качество

Junior-ready навык: уметь **быстро проверить**, что изменения не сломали поведение. Для этого нужны тесты и “привычка прогонять их” локально и в CI.

## 🎯 Цели урока

- Понять, что такое unit vs integration тесты (очень кратко)
- Написать первые тесты на `pytest`
- Познакомиться с fixtures (`@pytest.fixture`)
- Запускать тесты локально и в GitHub Actions

## 🧠 Минимальная теория

### Что тестировать

- **Unit**: чистые функции (вход → выход), без сети/файлов/БД
- **Integration (smoke)**: один “простой” тест, который проверяет работу приложения “снаружи” (например HTTP endpoint)

### Правило “пирамиды”

Много unit-тестов, мало integration-тестов.

## 🧪 Примеры

См. папку `examples/`:

- `calc.py` + `test_calc.py` — unit тесты функций (запуск: `cd examples && pytest test_calc.py`)
- `app.py` + `test_app.py` — простой API тест через `TestClient` (нужны `pip install fastapi httpx`, затем `pytest test_app.py`)

## 🏠 Домашнее задание

См. [homework.md](homework.md).

## 🤖 Промпты для AI

См. [prompts.md](prompts.md).

