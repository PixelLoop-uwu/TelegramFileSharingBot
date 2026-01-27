## Telegram File Sharing Bot

TelegramFileSharingBot — это проект для обмена файлами через Telegram-бота с возможностью хранения, скачивания и автоматического удаления файлов. Включает Telegram-бота (Aiogram) и backend API (FastAPI).

### Возможности
- Загрузка и хранение файлов пользователями Telegram
- Получение списка файлов и скачивание по ссылке
- Ограничение на количество файлов и автоудаление старых
- Админ-панель и гибкая настройка через config.toml

### Технологии
- Python 3.11+
- [aiogram](https://github.com/aiogram/aiogram) — Telegram Bot API
- [FastAPI](https://fastapi.tiangolo.com/) — backend API
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM для работы с БД
- [APScheduler](https://apscheduler.readthedocs.io/) — планировщик задач
- [aiofiles, loguru, python-dotenv, requests, humanize, uvicorn]

### Установка и запуск
1. Клонируйте репозиторий и перейдите в папку проекта:
	```bash
	git clone ...
	cd TelegramFileSharingBot
	```
2. Установите зависимости (лучше в venv):
	```bash
	python -m venv venv
	venv\Scripts\activate  # Windows
	pip install -r requirements.txt  # или используйте pyproject.toml
	```
3. Создайте файл `.env` и укажите токен бота:
	```env
	bot_token=ВАШ_ТОКЕН_БОТА
	```
4. Проверьте и настройте параметры в `config.toml` (пути, лимиты, порты и т.д.)
5. Установите проект:
	```bash
	python install.py
	```

### Структура проекта
- `bot/` — Telegram-бот (aiogram)
- `api/` — backend API (FastAPI)
- `shared/` — общие настройки 
- `config.toml` — основные параметры
- `install.py` — скрипт инициализации

### Примечания
- Для работы нужен Python >= 3.11
- Все зависимости указаны в pyproject.toml
- Для production рекомендуется запускать API через uvicorn/gunicorn, а бота — в отдельном процессе

---
Автор: [ваше имя или ссылка]
