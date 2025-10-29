# :snowman: Telegram file share bot

<!-- <h3>Написан на 
  <img src="https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=%2361DAFB" alt="Python" style="vertical-align: middle;">
</h3> -->

### Бот для удобного обмена файлами через Telegram. Позволяет загружать файлы, получать короткие ссылки и делиться ими с другими пользователями.

---

## 1. Функционал:
- Загрузка файлов в бота  
- Получение ссылки на скачивание  
- Поддержка разных форматов файлов  
- Возможность удаления файлов
- Авто-удаление старых файлов спустя неделю


## 2. Библиотеки:
- Бот - [Aiogram](https://github.com/aiogram/aiogram)
- Апи - [FasApi](https://github.com/fastapi)
- Базы данных - [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)

<!-- ## 3. Зависимости:
- Свой домен
- Пакеты: 
```sh
python3 python3-pip python3-venv nginx certbot
``` -->

## 4. Установка: 
```sh
# Клонируйте репозиторий
git clone https://github.com/PixelLoop-uwu/TelegramFileSharingBot
cd TelegramFileSharingBot

# Создайте виртуальное окружение
python3 -m venv venv
source venv/bin/active

# Загрузите все нужные пакеты
pip install -r requests.txt
```

## 5. Конфигуация:
```sh
# Создайте .env с токенои бота
echo BOT_TOKEN="<токен>" > bot/.env

# Отредактируйте конфигурацию бота/апи
vim cfg.py
```

## 6. Использование
- Для загрузки файлов просто отправьте его в чат
- /start - Просмотр списока файлов

# ...
