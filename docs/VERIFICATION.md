# Проверка ссылок и материалов

*Дата проверки: март 2026*

## Внутренние ссылки (файлы)

| Откуда | Ссылка | Статус |
|--------|--------|--------|
| module-00-intro/lesson-01-what-is-vibecoding.md | ../resources/translations/vibe-coding-guide-ru.md | ✅ |
| module-00-intro/lesson-02-why-devops-matters.md | ../resources/translations/12-factor-app-ru.md | ✅ |
| module-00-intro/resources.md | ../resources/translations/*.md | ✅ |
| module-02-tools/lesson-03-cursor-setup/README.md | ../../integrations/agency-agents.md | ✅ |
| module-01-basics/lesson-01-variables/README.md | ../../resources/translations/python-variables-ru.md | ✅ |
| module-01-basics/lesson-01-variables/README.md | ../../resources/translations/python-data-types-ru.md | ✅ |
| community/useful-links.md | ../resources/translations/*.md | ✅ |
| resources/translations/README.md | 12-factor-app-ru.md, python-variables-ru.md и др. | ✅ |

## Файлы в resources/translations/

| Файл | Существует |
|------|------------|
| 12-factor-app-ru.md | ✅ |
| python-variables-ru.md | ✅ |
| python-data-types-ru.md | ✅ |
| vibe-coding-guide-ru.md | ✅ |
| README.md | ✅ |

## Соответствие источникам

### 12 Factor App (12factor.net)
- Все 12 факторов присутствуют и корректно переведены
- Соответствует оригиналу и [русской версии](https://12factor.net/ru/)

### Python Variables (W3Schools)
- Переменные, имена, присваивание, global — всё покрыто
- Добавлен блок «Важно для работы с AI» (input → строка)

### Python Data Types (Real Python)
- int, float, str, bool, type(), isinstance(), преобразования — всё покрыто
- Добавлено предупреждение про input()

### Vibe Coding (VibeCodingLearn, Google Cloud)
- Определение, процесс, сравнение с традиционным — всё покрыто
- Статистика 45% уязвимостей — подтверждена [Veracode 2025 GenAI Code Security Report](https://www.veracode.com/blog/genai-code-security-report/)
- Инструменты (Cursor, Claude, Copilot) — актуальны

## Внешние ссылки (проверены)

| URL | Статус |
|-----|--------|
| https://12factor.net/ | ✅ |
| https://12factor.net/ru/ | ✅ |
| https://www.w3schools.com/python/python_variables.asp | ✅ |
| https://realpython.com/python-data-types/ | ✅ |
| https://vibecodinglearn.com/what-is-vibe-coding | ✅ |
| https://cloud.google.com/discover/what-is-vibe-coding | ✅ |
| https://github.com/msitarzewski/agency-agents | ✅ |

## Исправления внесённые при проверке

- `module-02-tools/lesson-03-cursor-setup/README.md`: ссылка «Подробнее» — текст изменён с пути на «интеграция agency-agents»
