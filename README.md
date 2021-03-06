Репозиторий учебного интернет-магазина на **Django 3**.

Установка:

1. Склонируйте к себе данный репо при помощи команды:

    ```code
    git clone https://github.com/Sordun/Django3_web.git
    ```

1. Выполните команду для создания виртуального окружения:

    ```code
    python -m venv env
    ```

1. Активируйте созданное виртуальное окружение при помощи команды:

    ```code
    env\Scripts\activate
    ```

1. Установите необходимые пакеты в активированное окружение при помощи команды:

    ```code
    pip install -r requirements.txt
    ```

1. Перейдите в папку проекта:

    ```code
    cd Shop
    ```

1. Проведите миграции БД при помощи команды:

    ```code
    python manage.py migrate
    ```

1. Запустите проект при помощи команды (по умолчанию запускается на 8000 порту, если на вашей машине он занят, то используйте любой незанятый):

    ```code
    python manage.py runserver
    ```

1. Перейдите на страницу <http://127.0.0.1:8000/api> (или ваш собственный порт)


1. Не забудьте создать директорию **media**, куда будут сохраняться изображения для товара
