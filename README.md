# Telegram Bot для скачивания MP3/MP4 с YouTube

## Описание

Этот проект представляет собой Telegram бота, который позволяет пользователям скачивать аудио (MP3) и видео (MP4) файлы с YouTube.

## Установка

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/medlcago/TgBotYouTube
    ```
2. Установите необходимые зависимости:
    ```
    pip install -r requirements.txt
    ```
3. Создайте файл `.env` и укажите в нем токен вашего бота:
    ```
    BOT_TOKEN=your_bot_token
    ```
4. Запустите бота:
    ```
    python main.py
    ```

## Использование

1. Откройте Telegram и найдите вашего бота по имени.
2. Введите URL или название видео на YouTube, которое вы хотите скачать.
3. Выберите формат файла (MP3 или MP4).
4. Бот отправит вам файл или ссылку для скачивания, если размер файла превышает максимально допустимый размер для отправки в Telegram.