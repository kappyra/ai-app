# ai-app

Учебное Flask-приложение для практической работы по Docker: конфигурация через
переменные окружения, логи в `/app/logs`, ответ на `/` и `/health`.

## Переменные окружения

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `APP_MESSAGE` | `AI app запущено` | текст на главной странице |
| `APP_PORT` | `8000` | порт приложения |

## Локальный запуск

```bash
docker build -t ai-app:local .
docker run -d --name ai-app -p 8000:8000 ai-app:local
curl http://localhost:8000
```

## Публикация через GitHub Actions

Workflow `.github/workflows/docker.yml` собирает образ и публикует его
в GitHub Container Registry при push в `main` и при создании тега `v*`.

Теги образа: `ghcr.io/<owner>/ai-app:latest` и `ghcr.io/<owner>/ai-app:<sha>`.
