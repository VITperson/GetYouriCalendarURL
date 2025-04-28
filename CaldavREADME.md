# get_caldav_url

## Описание приложения
Скрипт на Python, который подключается к вашему iCloud-аккаунту по протоколу CalDAV и выводит список ваших календарей с их именами и URL-адресами.

## Цель
Помочь быстро узнать точные CalDAV-URL ваших календарей в iCloud для дальнейшей работы с ними (например, создания или чтения событий через API).

## Предусловия
Перед запуском убедитесь, что у вас есть:
1. Аккаунт Apple ID с **App-Specific Password** (специальный пароль для сторонних приложений).
2. Установленный Python 3.7+ и доступ к `pip`.
3. Доступ в интернет (CalDAV-сервер iCloud доступен по адресу `https://caldav.icloud.com/`).

## Установка

1. Склонируйте репозиторий (или скопируйте файл):
   ```bash
   git clone https://github.com/ваш-репозиторий/….git
   cd ваш-репозиторий
   ```
2. Создайте и активируйте виртуальное окружение (рекомендуется):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   .venv\Scripts\activate.bat     # Windows
   ```
3. Установите зависимости:
   ```bash
   pip install caldav python-dotenv
   ```
   > Если у вас есть `requirements.txt`, можно выполнить:
   > ```bash
   > pip install -r requirements.txt
   > ```

## Настройка

1. В корне проекта создайте файл `.env` со следующими переменными:
   ```dotenv
   ICLOUD_USER=ваш_apple_id@example.com
   ICLOUD_APP_PW=ваш_app_specific_password
   ```
2. При необходимости отредактируйте URL сервера в начале скрипта (по умолчанию для iCloud):
   ```python
   client = DAVClient(
       url="https://caldav.icloud.com/",
       username=os.getenv("ICLOUD_USER"),
       password=os.getenv("ICLOUD_APP_PW")
   )
   ```

## Запуск

```bash
python get_caldav_url.py
```

После запуска вы увидите в консоли примерно такой вывод:

```
Имя: Личные
URL: https://caldav.icloud.com/.../calendars/...
Имя: Работа
URL: https://caldav.icloud.com/.../calendars/...
...
```

## Что дальше
Используйте полученные URL в своих скриптах для создания, чтения или удаления событий через CalDAV-API.

---

