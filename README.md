Требования
- Docker Desktop
- Python 3.9+

Установка
bash
git clone https://github.com/Xermitt/doctor_appointment.git

cd doctor_appointment

docker-compose up --build


ПЕРВЫЙ запуск

    Создайте суперпользователя:
    bash
    docker exec -it doctor_appointment-web-1 python manage.py createsuperuser

    Примените миграции:
    bash
    docker exec -it doctor_appointment-web-1 python manage.py migrate


API Endpoints
Примеры запросов (Postman)
GET Запросы:

Получить все записи:
GET http://localhost:8000/api/appointments/

Получить всех врачей
GET http://localhost:8000/api/doctors/

Получить всех пациентов
GET http://localhost:8000/api/patients/

Получить конкретную запись (ID=1):
GET http://localhost:8000/api/appointments/1/

POST Запрос (создание записи):
POST http://localhost:8000/api/appointments/

{
    "patient": 1,
    "doctor": 1,
    "date": "2024-05-21",
    "time": "10:00:00"
}

здесь можно ввести разные данные на свое усмотрение, проверить на ошибки(например запись на ночь) и также создать запись


пример вывода ошибки:
Ошибка при дублировании записи:

json
{
    "non_field_errors": [
        "The fields doctor, date, time must make a unique set."
    ]
}


Доступ
http://localhost:8000/admin/

Логин:admin
Пароль:qwerty12345ASD