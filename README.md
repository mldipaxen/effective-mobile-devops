Тестовое задание, Effective Mobile

1. Запуск контейнеров
docker compose up -d --build
Ждите 10-15 секунд
2. По команде curl http://localhost вывод будет:
Hello from Effective Mobile!
3. Проверка изоляции
curl http://localhost:8080
Ожидается отказ в соединении. Это подтверждает корректную настройку сети.
3. Просмотр логов
docker compose logs -f
Структура проекта
.
├── backend/
│   ├── app.py          # Python HTTP-сервер
│   └── Dockerfile      # Сборка backend-образа
├── nginx/
│   └── nginx.conf      # Конфигурация reverse proxy
├── docker-compose.yml  # Оркестрация сервисов
├── .env                # Переменные окружения (версии, порты, лимиты)
├── .gitignore         
└── README.md          
							Технологии
Docker и Docker Compose
Python 3.12-slim (официальный минимальный образ)
Nginx 1.25-alpine (официальный минимальный образ)
Изолированная Docker-сеть (bridge driver)
Healthchecks для контроля готовности сервисов

		Помимо требований ТЗ, реализованы следующие меры для повышения надёжности и безопасности:
1) Безопасность контейнеров
2) Запуск backend от непривилегированного пользователя appuser
3) Файловая система контейнеров переведена в режим read_only, временные директории вынесены в tmpfs
4) Опция no-new-privileges:true запрещает повышение прав внутри контейнера
5) Удаление лишних Linux-капабилити (cap_drop: [ALL]) для backend
6) Скрытие версии Nginx в HTTP-заголовках (server_tokens off)

- Реализован graceful shutdown в Python-приложении (корректная обработка SIGTERM)
- Healthchecks в Dockerfile и docker-compose.yml с настройкой интервала, таймаута и периода запуска
- Зависимость depends_on: condition: service_healthy гарантирует запуск nginx только после готовности backend
- Ограничение размера логов (ротация: 10 МБ на файл, максимум 3 файла)
Управление ресурсами и конфигурацией
Явные лимиты CPU и памяти для каждого сервиса через deploy.resources.limits
Вынос конфигурируемых параметров (версии образов, порты, лимиты) в файл .env для удобства управления окружениями
P.S. Для корректной работы ci в docker-compose.yml были добавлены дефолтные значения переменных
