Сначала редактируем файл .env

DEBUG=True <- Горячая перезагрузка в случае изменений при деплое на боевой сервак False

CORS_ALLOWED_ORIGINS='localhost' <- если ошибка CORS сюда ip адрес или домен с http
CSRF_TRUSTED_ORIGINS='localhost'<- если ошибка CSRF сюда ip адрес или домен с http

Базы данных ПОСТГРЕС
NAME='имя базы данных'
USER='имя пользователя'
PASSWORD='пароль пользователя'
HOST='Адрес БД'
PORT='Порт БД'

Разворачиваем проект командой
docker-kompose up --build

проверка доступности
0.0.0.0:8000