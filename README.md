# course_website

Веб-сайт для продажи онлайн-курсов на Django с регистрацией пользователей и Bootstrap-дизайном.

---

## Требования

- Python 3.8+
- Django 5.2.1 (или совместимая версия)

---

## Установка и запуск

1. Клонируйте репозиторий (если есть) или скачайте файлы проекта.

2. Создайте и активируйте виртуальное окружение (рекомендуется):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install django

cd course_website
python manage.py migrate


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver


Главная страница: http://127.0.0.1:8000/

Регистрация: http://127.0.0.1:8000/register/

Вход: http://127.0.0.1:8000/login/

Админка: http://127.0.0.1:8000/admin/

