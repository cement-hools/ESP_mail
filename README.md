# ESP_mail
ТЗ 
1. Пользоватлеь заходит на сайт 
2. Пользователь игает в игру 
3. Пользователь оставляет свою почту 
4. Бекенд принимает почту 
5. Бекенд смотрит в свою базу играла почта или нет 
6. Если в базе игры почты нет: Бекенд проверяет в ESP системе 
есть такая почта или нет Если потчы нет, создает ее в ESP системе 
Бекенд записывает в свою базу факт игры 
7. Если в базе игры почта есть бекенд инкрементит в базе кол. игр 
8. Бекенд возвращает на фронт результат: 
- Почта была в ESP или нет 
- Почта была в базе игры или нет 
- Кол. игр с учетом этой игры 

Что нужно сделать 
1. Создать проект и описать структуру папок. 
В письменном обосновать выбранный фреймворк и описать структуру проекта. 
Отталкивайтесь от того, что проект будет дополняться новым функционалом 
2. Реализовать ендпоинт описанный в тз 
3. Для обращения к ESP написать интерфейс (ABC, Protocol, etc.) 
4. Написать моковую имплементацию написанного выше интерфейса

### endpoint
- **POST**```/api/verification_mail/``` Отправить email пользователя на сервер.
```json
{
    "email": "cem@test.ru"
}
```
#### ответ
если email нет в базе игр и в esp
```json
{
    "esp_status": false,
    "games_status": false,
    "games_count": 1
}
```
если email уже играл
```json
{
    "esp_status": true,
    "games_status": true,
    "games_count": 5
}
```

## Установка и запуск на сервере разработчика
1. Клонировать репозиторий
    ```
    git clone https://github.com/cement-hools/ESP_mail
    ```
2. Перейдите в директорию ESP_mail
    ```
   cd ESP_mail
    ```
3. Создать виртуальное окружение, активировать и установить зависимости
    ``` 
   python -m venv venv
    ```
   Варианты активации окружения:
   - windows ``` venv/Scripts/activate ```
   - linux ``` venv/bin/activate ```
     <br><br>
   ```
   python -m pip install -U pip
   ```
   ```
   pip install -r requirements.txt
   ```
4. Выполните миграции
   ```
   python manage.py migrate
   ```
5. Создать супер юзера
   ```
   python manage.py createsuperuser
   ```
6. Запустить приложение на сервере разработчика
   ```
   python manage.py runserver
   ```
7. Проект доступен 
   ```
   http://127.0.0.1:8000/
   http://localhost:8000/
   ```

## Запуск в трех контейнерах (PostgreSQL, Web, Nginx)

1. Клонировать репозиторий
    ```
    git clone https://github.com/cement-hools/ESP_mail
    ```
2. Перейдите в директорию ESP_mail
    ```
   cd ESP_mail
    ```
3. Запустить docker-compose
    ```
    docker-compose up --build
    ```
4. Зайти в контейнер и выполнить миграции
    ```
    docker-compose exec web python manage.py migrate --noinput
    ```
5. Зайти в контейнер и создать супер юзера.
    ```
    docker-compose exec web python manage.py createsuperuser
    ```
7. Проект доступен 
   ```
   http://127.0.0.1/
   http://localhost/
   ```
