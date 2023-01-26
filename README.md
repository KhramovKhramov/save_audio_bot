# save_audio_bot

Этот telegram-бот умеет сохранять из чатов картинки, аудиозаписи и войсы. Каждого пользователя бот добавляет в базу данных MongoDB, туда же (с привязкой к конкретному пользователю), складывает изображения, войсы и аудио в бинарном формате. Все аудиозаписи и войсы бот сначала переводит в формат .wav, а все изображения сначала проверяет с помощью clarifai и сохраняет только те, где есть лицо. 

Кроме того, все файлы бот сохраняет в отдельную папку на сервере (с разбивкой по конкретным пользователям). 

## Документация

Бот написан на библиотеке python-telegram-bot, используются возможности clarifai, pydub, MongoDB.

1. [Документация python-telegram-bot](https://python-telegram-bot.org/)
2. [python-telegram-bot на GitHub](https://github.com/python-telegram-bot/python-telegram-bot)
3. [Возможности Clarifai](https://clarifai.com/explore)
4. [pydub](http://pydub.com)
5. [MongoDB](https://www.mongodb.com/docs/)

## Настройка

1. Выполните в консоли команды:
```
#клонируем репозиторий:
git clone https://github.com/KhramovKhramov/save_audio_bot.git

#создаем виртуальное окружение (пример для MacOS):
python3 -m venv .venv

#активируем виртуальное окружение (пример для MacOS):
source .venv/bin/activate

#устанавливаем зависимости:
pip install -r requirements.txt
```
2. Создайте в корне проекта файл settings.py и добавьте туда следующие настройки:
```
API_KEY = 'API-ключ вашего Telegram-бота, который вам выдал бот BotFather'
MONGO_LINK = 'Ключ к вашей базе данных MongoDB'
NAME_DB = 'Имя вашей базы данных'
CLARIFAI_API_KEY = 'API-ключ вашего проекта Clarifai'
```
## Запуск

Запутите команду при активированном виртуальном окружении:
```
python main.py
```
