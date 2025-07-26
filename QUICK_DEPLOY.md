# 🚀 Быстрый деплой сайта

## Вариант 1: Railway.app (Рекомендуется)

### Шаги:
1. **Перейдите на [railway.app](https://railway.app)**
2. **Войдите через GitHub**
3. **Нажмите "New Project"**
4. **Выберите "Deploy from GitHub repo"**
5. **Выберите репозиторий:** `C-gen/autopicker`
6. **Railway автоматически определит Django проект**
7. **Добавьте переменные окружения:**
   - `SECRET_KEY`: любая случайная строка
   - `DEBUG`: `False`
8. **Нажмите "Deploy Now"**

### Результат:
- ✅ Сайт будет доступен по адресу: `https://your-app-name.railway.app`
- ✅ База данных создается автоматически
- ✅ SSL сертификат включен
- ✅ Домен можно настроить

---

## Вариант 2: Render.com

### Шаги:
1. **Перейдите на [render.com](https://render.com)**
2. **Войдите через GitHub**
3. **Нажмите "New +" → "Web Service"**
4. **Подключите репозиторий:** `C-gen/autopicker`
5. **Настройки:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn autopicker.wsgi:application`
6. **Создайте PostgreSQL базу данных**
7. **Добавьте переменную:** `DATABASE_URL`
8. **Нажмите "Create Web Service"**

### Результат:
- ✅ Сайт будет доступен по адресу: `https://your-app-name.onrender.com`
- ⚠️ Бесплатный план имеет ограничения

---

## Вариант 3: PythonAnywhere (Бесплатно)

### Шаги:
1. **Перейдите на [pythonanywhere.com](https://pythonanywhere.com)**
2. **Создайте бесплатный аккаунт**
3. **В консоли выполните:**
   ```bash
   git clone https://github.com/C-gen/autopicker.git
   cd autopicker
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
4. **Настройте WSGI файл**
5. **Создайте веб-приложение**

### Результат:
- ✅ Сайт будет доступен по адресу: `your-username.pythonanywhere.com`
- ⚠️ Ограниченная производительность

---

## 🔗 GitHub репозиторий

**Ссылка на код:** https://github.com/C-gen/autopicker

---

## 📝 После деплоя

1. **Откройте админ-панель:** `/admin/`
2. **Создайте суперпользователя:**
   ```bash
   python manage.py createsuperuser
   ```
3. **Добавьте контент:**
   - Настройки сайта
   - Услуги
   - Отзывы
   - Статьи блога

---

## 🆘 Проблемы?

- **Проверьте логи** в панели управления хостинга
- **Убедитесь, что все переменные окружения настроены**
- **Проверьте, что миграции выполнены**

---

## 🎯 Рекомендация

**Для быстрого деплоя используйте Railway.app** - это самый простой способ с автоматической настройкой базы данных и SSL. 