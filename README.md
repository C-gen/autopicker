# Автоподбор - Сайт специалиста по подбору автомобилей

Современный и адаптивный сайт для специалиста по автоподбору автомобилей, созданный на Django.

## Функциональность

- **Главная страница** с описанием услуг и преимуществ
- **Страница "Обо мне"** с информацией о специалисте
- **Страница "Услуги"** с описанием пакетов услуг
- **Форма заявки** с отправкой на email
- **Отзывы клиентов** с рейтингами
- **Блог** с полезными статьями
- **Страница контактов** с формой обратной связи
- **Адаптивный дизайн** для всех устройств

## Технологии

- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **База данных**: SQLite (для разработки), PostgreSQL (для продакшена)
- **Email**: SMTP через Gmail
- **Деплой**: Vercel, Render или VPS

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd AutoResearch
```

### 2. Создание виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Скопируйте файл `env.example` в `.env` и настройте переменные:

```bash
cp env.example .env
```

Отредактируйте `.env` файл:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@autopicker.ru
```

### 5. Применение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Создание суперпользователя

```bash
python manage.py createsuperuser
```

### 7. Сбор статических файлов

```bash
python manage.py collectstatic
```

### 8. Запуск сервера разработки

```bash
python manage.py runserver
```

Сайт будет доступен по адресу: http://127.0.0.1:8000/

## Настройка контента

### 1. Админ-панель

Перейдите в админ-панель: http://127.0.0.1:8000/admin/

### 2. Настройки сайта

Создайте запись в разделе "Настройки сайта" с контактной информацией.

### 3. Добавление контента

- **Услуги**: Добавьте пакеты услуг в разделе "Услуги"
- **Отзывы**: Добавьте отзывы клиентов в разделе "Отзывы"
- **Блог**: Создайте статьи в разделе "Статьи блога"

## Деплой

### Vercel

1. Создайте файл `vercel.json`:

```json
{
  "builds": [
    {
      "src": "autopicker/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "autopicker/wsgi.py"
    }
  ]
}
```

2. Добавьте в `settings.py`:

```python
import os
if os.path.exists('vercel.json'):
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Render

1. Создайте файл `build.sh`:

```bash
#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

2. Настройте переменные окружения в панели Render.

### VPS

1. Установите nginx и gunicorn
2. Настройте nginx конфигурацию
3. Запустите через systemd

## Структура проекта

```
AutoResearch/
├── autopicker/          # Основной проект Django
├── main/               # Приложение с основным функционалом
├── templates/          # HTML шаблоны
├── static/            # Статические файлы
├── media/             # Загружаемые файлы
├── requirements.txt   # Зависимости Python
├── env.example        # Пример переменных окружения
└── README.md         # Документация
```

## Основные модели

- **Service**: Услуги автоподбора
- **Application**: Заявки клиентов
- **Review**: Отзывы клиентов
- **BlogPost**: Статьи блога
- **SiteSettings**: Настройки сайта

## Лицензия

MIT License

## Поддержка

Для получения поддержки обращайтесь к разработчику. 