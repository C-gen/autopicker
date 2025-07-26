from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Service(models.Model):
    """Модель для услуг автоподбора"""
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    duration = models.CharField(max_length=100, verbose_name="Срок выполнения")
    features = models.JSONField(default=list, verbose_name="Особенности услуги")
    is_popular = models.BooleanField(default=False, verbose_name="Популярная услуга")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ['price']

    def __str__(self):
        return self.name


class Application(models.Model):
    """Модель для заявок клиентов"""
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('processing', 'В обработке'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    budget = models.CharField(max_length=100, verbose_name="Бюджет")
    brand_model = models.CharField(max_length=200, verbose_name="Марка/модель")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.brand_model}"


class Review(models.Model):
    """Модель для отзывов клиентов"""
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка"
    )
    text = models.TextField(verbose_name="Текст отзыва")
    car_model = models.CharField(max_length=200, blank=True, verbose_name="Модель автомобиля")
    is_verified = models.BooleanField(default=False, verbose_name="Проверенный отзыв")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"


class BlogPost(models.Model):
    """Модель для статей блога"""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    content = models.TextField(verbose_name="Содержание")
    excerpt = models.TextField(max_length=300, blank=True, verbose_name="Краткое описание")
    image = models.ImageField(upload_to='blog/', blank=True, verbose_name="Изображение")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.excerpt and self.content:
            self.excerpt = self.content[:300] + "..." if len(self.content) > 300 else self.content
        super().save(*args, **kwargs)


class SiteSettings(models.Model):
    """Модель для настроек сайта"""
    site_name = models.CharField(max_length=100, default="Автоподбор", verbose_name="Название сайта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    telegram = models.CharField(max_length=100, blank=True, verbose_name="Telegram")
    whatsapp = models.CharField(max_length=100, blank=True, verbose_name="WhatsApp")
    address = models.TextField(blank=True, verbose_name="Адрес")
    inn = models.CharField(max_length=12, blank=True, verbose_name="ИНН")
    ogrn = models.CharField(max_length=15, blank=True, verbose_name="ОГРН")
    about_text = models.TextField(blank=True, verbose_name="О компании")
    about_image = models.ImageField(upload_to='about/', blank=True, verbose_name="Фото о компании")
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            return
        super().save(*args, **kwargs)
