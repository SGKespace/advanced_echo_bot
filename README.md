# advanced_echo_bot
Боты автоматически отвечающие пользователю в Телеграм и ВК. Если возникает ошибка приходит сообщение в Телеграм бот (TELEGRAM_TOKEN_LOG, TG_CHAT_ID_LOG см. файл .env)

Пример работы в Телеграм 

https://github.com/SGKespace/advanced_echo_bot/assets/55636018/445989d8-3fef-4a32-8a46-ef4623b53c91



Пример работы в ВК

https://github.com/SGKespace/advanced_echo_bot/assets/55636018/092631be-86d7-468f-bb37-fe5c1f968bda


## Требования к окружению

Получите токены  [Телеграм](https://t.me/BotFather), затем определите [chat_id](https://t.me/messageinformationsbot)  поместите в переменные окружения (файл .env). ВК: в меню управления сообщества на вкладке API. [Сайт DialogFlow для проекта](https://dialogflow.cloud.google.com/#/login)

Пример файла:

```
TELEGRAM_TOKEN="63576433268:AAECYahvjljghkh7685694"
TELEGRAM_TOKEN_LOG="63576433268:AAECYahvjljghkh7685694"
TG_CHAT_ID_LOG=123456789
GOOGLE_CLOUD_PROJECT="ert-dfg"
GOOGLE_APPLICATION_CREDENTIALS='/Users/sgk/.config/gcloud/credentials.json'
VK_TOKEN='vk1.a.ldsdgdvgsvc9-5nsgHA9_lkOxEGGJGJGxF-ZtWJHGGUYTfajmak6yosrqEKvGCWWGHJggjhlkhluiOHvRiRI2q7HQr7Jwpbx4k1E79Qs9PKbBY-a3BgHGJHGKGGGKJJKHKbkgkgleF0lZEv0e4usc74Cfc_YG-z3ZDYn5FJCJHHKJHggjgjgGKHLIIYHhZ9U5lczxZlw'

``` 

Python 3.xx и выше (должен быть уже установлен)

``` 
google-cloud-dialogflow==2.23.2
python-dotenv==1.0.0
python-telegram-bot==13.14
requests==2.28.1
vk-api==11.9.9
``` 

Можно установить командой  
``` 
PIP install -r requirement.txt
```

Запускать ботов осууществляетс с помощью команд

``` 
python tg_bot.py
python vk_bot.py
```

# "Тренировка" бота
Рзместите файл questions.json рядом с create_intent.py
Натренировать бота можно с помощью скрипта create_intent.py, который запускается следующей командой

``` 
python create_intent.py
``` 

# Описание файлов
- tg_bot.py скрипт автоответчика в Телеграм
- vk_bot.py скрипт автоответчика в ВК
- requirements.txt пример файла для тренировки Google DialogFlow
- create_intent.py скрипт для тренировки Google DialogFlow
- questions.json пример файла для тренировки

## Отказ от ответственности

Автор программы не несет никакой ответственности за то, как вы используете этот код или как вы используете сгенерированные с его помощью данные. Эта программа была написана для обучения автора и других целей не несет. Не используйте данные, сгенерированные с помощью этого кода в незаконных целях.
