# Домашнее задание: GitHub Actions

## Задание A (обязательно): CI workflow

1) Создайте `.github/workflows/test.yml`  
2) Добавьте шаг запуска тестов (`pytest`) или хотя бы `echo` (если тестов пока нет)  
3) Сделайте push и проверьте, что workflow выполнился  

## Задание B (желательно): deploy workflow

1) Создайте `.github/workflows/deploy.yml` с триггером на `push` в `main`  
2) Добавьте шаг деплоя (deploy hook / CLI платформы)  
3) Все токены/URL храните в GitHub Secrets  

## Критерии сдачи

- [ ] CI workflow есть и успешно проходит на push/PR
- [ ] (Желательно) CD workflow есть и запускается на push в main
- [ ] Секретов нет в репозитории
