# LPR Parking API

## Как это работает
На сервере должен быть установлен docker и docker-compose

### Настройки в файле .env

- `DEBUG`=True - Горячая перезагрузка в случае изменений при деплое на боевой сервак False
- `CORS_ALLOWED_ORIGINS`=localhost - если ошибка CORS сюда ip адрес или домен с http
- `CSRF_TRUSTED_ORIGINS`=localhost - если ошибка CSRF сюда ip адрес или домен с http

Настройки подключения к PostgreSQL
- `NAME`='имя базы данных'
- `USER`='имя пользователя'
- `PASSWORD`='пароль пользователя'
- `HOST`='Адрес БД'
- `PORT`='Порт БД'

### Настройки в файле entrypoint.sh

- `gunicorn config.wsgi:application --bind 0.0.0.0:8000` - здесь можно отредактировать бинд на запуск по какому адресу
(`0.0.0.0:8000` стандартный запуск)

### Запуск
 - `docker-compose up --build`

### Проверка доступности
- Открыть в браузере `http://0.0.0.0:8000`
- 