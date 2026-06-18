# 💧 Water Tracker

Сервис для отслеживания потребления воды с автоматической коррекцией дневной нормы на основе погоды. Помогает поддерживать водный баланс с учётом веса, возраста, физической активности и температуры воздуха.

## Технологии
* **Python 3.14**
* **Django 6.0.6**
* **OpenWeatherMap API**
* **Bootstrap 5**

## Скриншоты
![Страница регистрации](screenshots/регистрация.png)
*Страница регистрации нового пользователя*

![Страница входа](screenshots/вход.png)
*Страница входа пользователя*

![Главная страница](screenshots/оснстр.png)
*Главная страница с трекером воды и прогрессом*

![Добавление/удаление воды](screenshots/добавление.png)
*Кнопки добавления и удаления*

## Как запустить проект локально
1. **Клонируйте репозиторий:**
   ```bash
   git clone ![https://github.com/Olinka-frog/water-tracker-django.git](https://github.com/Olinka-frog/water-tracker-django.git)
   ```
2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # для Linux/Mac
   venv\Scripts\activate     # для Windows
   ```
3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Выполните миграции:**
   ```bash
   python manage.py migrate
   ```
5. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```
6. **Откройте проект в браузере:**
   Перейдите по ссылке: http://127.0.0.1:8000/