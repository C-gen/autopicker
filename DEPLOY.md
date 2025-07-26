# Инструкция по деплою на Render.com

## 🚀 Быстрый деплой

### 1. Подготовка
- ✅ Код уже загружен на GitHub: https://github.com/C-gen/autopicker
- ✅ Все необходимые файлы созданы

### 2. Деплой на Render.com

1. **Перейдите на [render.com](https://render.com)**
2. **Зарегистрируйтесь/войдите** (можно через GitHub)
3. **Нажмите "New +" → "Web Service"**
4. **Подключите GitHub репозиторий:**
   - Выберите репозиторий: `C-gen/autopicker`
   - Branch: `main`

### 3. Настройки сервиса

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
gunicorn autopicker.wsgi:application
```

**Environment Variables:**
- `SECRET_KEY`: (автоматически сгенерируется)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `your-app-name.onrender.com`

### 4. База данных

1. **Создайте PostgreSQL базу данных:**
   - "New +" → "PostgreSQL"
   - Выберите план "Free"
   - Название: `autopicker-db`

2. **Подключите базу к веб-сервису:**
   - В настройках веб-сервиса → "Environment"
   - Добавьте переменную: `DATABASE_URL` (скопируйте из настроек PostgreSQL)

### 5. Запуск

1. **Нажмите "Create Web Service"**
2. **Дождитесь завершения деплоя** (5-10 минут)
3. **Выполните миграции:**
   - В консоли Render: "Shell"
   - Выполните команды:
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser
   ```

### 6. Настройка контента

1. **Откройте админ-панель:** `https://your-app-name.onrender.com/admin/`
2. **Создайте суперпользователя** (если еще не создали)
3. **Добавьте контент:**
   - SiteSettings (настройки сайта)
   - Services (услуги)
   - Reviews (отзывы)
   - BlogPosts (статьи блога)

## 🔧 Альтернативный деплой через render.yaml

Если у вас есть аккаунт на Render, можно использовать автоматический деплой:

1. **Создайте новый Blueprint Instance**
2. **Подключите репозиторий**
3. **Render автоматически создаст все сервисы**

## 📝 Важные замечания

- **Бесплатный план Render** имеет ограничения:
  - 750 часов в месяц
  - Сервис "засыпает" после 15 минут неактивности
  - Первый запрос может занять 30-60 секунд

- **Для продакшена рекомендуется:**
  - Платный план Render
  - Настройка домена
  - SSL сертификат
  - CDN для статических файлов

## 🔗 Полезные ссылки

- [GitHub репозиторий](https://github.com/C-gen/autopicker)
- [Render.com](https://render.com)
- [Django документация](https://docs.djangoproject.com/)
- [Render документация](https://render.com/docs)

## 🆘 Поддержка

Если возникли проблемы:
1. Проверьте логи в Render Dashboard
2. Убедитесь, что все переменные окружения настроены
3. Проверьте, что база данных подключена
4. Убедитесь, что миграции выполнены 