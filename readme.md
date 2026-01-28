## Telegram File Sharing Bot

TelegramFileSharingBot — это проект для обмена файлами через Telegram-бота с возможностью хранения, скачивания и автоматического удаления файлов. Включает Telegram-бота (Aiogram) и backend API (FastAPI).

### Возможности
- Загрузка и хранение файлов пользователями Telegram
- Получение списка файлов и скачивание по ссылке
- Ограничение на количество файлов и автоудаление старых

### Технологии
- Python 3.11+
- [aiogram](https://github.com/aiogram/aiogram) — Telegram Bot API
- [FastAPI](https://fastapi.tiangolo.com/) — backend API
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM для работы с БД
- [APScheduler](https://apscheduler.readthedocs.io/) — планировщик задач
- [aiofiles, loguru, humanize, uvicorn]

### Установка и запуск
1. Клонируйте репозиторий и перейдите в папку проекта:
	```bash
	git clone https://github.com/PixelLoop-uwu/TelegramFileSharingBot
	cd TelegramFileSharingBot
	```
3. Создайте файл `.env` и укажите токен бота:
	```env
	bot_token=ВАШ_ТОКЕН_БОТА
 	app_token=ВСЕ_ЧТО_УГОДНО
	```
4. Проверьте и настройте параметры в `config.toml`
5. Настройте проксирование запросов с вашего домена (`config.toml <download_url>`) на указанный порт (`docker-compose.yaml <port>`)
6. Соберите контейнер:
	```bash
	docker compose up --build -d
	```

### Структура проекта
- `bot/` — Telegram-бот (aiogram)
- `api/` — backend API (FastAPI)
- `shared/` — общие настройки 
- `config.toml` — основные параметры
- `install.py` — скрипт инициализации

