from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Service, Application, Review, BlogPost, SiteSettings
from .forms import ApplicationForm, ContactForm


def home(request):
    """Главная страница"""
    services = Service.objects.filter(is_popular=True)[:3]
    reviews = Review.objects.filter(is_verified=True)[:6]
    blog_posts = BlogPost.objects.filter(is_published=True)[:3]
    site_settings = SiteSettings.objects.first()
    
    context = {
        'services': services,
        'reviews': reviews,
        'blog_posts': blog_posts,
        'site_settings': site_settings,
    }
    return render(request, 'main/home.html', context)


def about(request):
    """Страница о компании"""
    site_settings = SiteSettings.objects.first()
    
    context = {
        'site_settings': site_settings,
    }
    return render(request, 'main/about.html', context)


def services(request):
    """Страница услуг"""
    services = Service.objects.all()
    site_settings = SiteSettings.objects.first()
    
    context = {
        'services': services,
        'site_settings': site_settings,
    }
    return render(request, 'main/services.html', context)


def reviews(request):
    """Страница отзывов"""
    reviews = Review.objects.filter(is_verified=True)
    site_settings = SiteSettings.objects.first()
    
    context = {
        'reviews': reviews,
        'site_settings': site_settings,
    }
    return render(request, 'main/reviews.html', context)


def blog(request):
    """Страница блога"""
    posts = BlogPost.objects.filter(is_published=True)
    site_settings = SiteSettings.objects.first()
    
    context = {
        'posts': posts,
        'site_settings': site_settings,
    }
    return render(request, 'main/blog.html', context)


def blog_detail(request, slug):
    """Детальная страница статьи"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    site_settings = SiteSettings.objects.first()
    
    context = {
        'post': post,
        'site_settings': site_settings,
    }
    return render(request, 'main/blog_detail.html', context)


def application_form(request):
    """Обработка формы заявки"""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            
            # Отправка email уведомления
            try:
                site_settings = SiteSettings.objects.first()
                if site_settings and site_settings.email:
                    subject = f'Новая заявка на автоподбор от {application.name}'
                    message = f"""
                    Новая заявка на автоподбор:
                    
                    Имя: {application.name}
                    Телефон: {application.phone}
                    Бюджет: {application.budget}
                    Марка/модель: {application.brand_model}
                    Комментарий: {application.comment}
                    
                    Дата: {application.created_at.strftime('%d.%m.%Y %H:%M')}
                    """
                    
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [site_settings.email],
                        fail_silently=False,
                    )
            except Exception as e:
                # Логируем ошибку, но не прерываем процесс
                print(f"Ошибка отправки email: {e}")
            
            messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('main:home')
    else:
        form = ApplicationForm()
    
    site_settings = SiteSettings.objects.first()
    context = {
        'form': form,
        'site_settings': site_settings,
    }
    return render(request, 'main/application_form.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def ajax_application(request):
    """AJAX обработка заявки"""
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            
            # Отправка email уведомления
            try:
                site_settings = SiteSettings.objects.first()
                if site_settings and site_settings.email:
                    subject = f'Новая заявка на автоподбор от {application.name}'
                    message = f"""
                    Новая заявка на автоподбор:
                    
                    Имя: {application.name}
                    Телефон: {application.phone}
                    Бюджет: {application.budget}
                    Марка/модель: {application.brand_model}
                    Комментарий: {application.comment}
                    
                    Дата: {application.created_at.strftime('%d.%m.%Y %H:%M')}
                    """
                    
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [site_settings.email],
                        fail_silently=False,
                    )
            except Exception as e:
                print(f"Ошибка отправки email: {e}")
            
            return JsonResponse({
                'success': True,
                'message': 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.'
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors
            })
    
    return JsonResponse({'success': False, 'message': 'Неверный метод запроса'})


def contact(request):
    """Страница контактов"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Отправка сообщения
            try:
                site_settings = SiteSettings.objects.first()
                if site_settings and site_settings.email:
                    subject = f'Сообщение с сайта: {form.cleaned_data["subject"]}'
                    message = f"""
                    Сообщение от: {form.cleaned_data['name']}
                    Email: {form.cleaned_data['email']}
                    
                    Сообщение:
                    {form.cleaned_data['message']}
                    """
                    
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [site_settings.email],
                        fail_silently=False,
                    )
            except Exception as e:
                print(f"Ошибка отправки email: {e}")
            
            messages.success(request, 'Ваше сообщение отправлено! Мы ответим вам в ближайшее время.')
            return redirect('main:contact')
    else:
        form = ContactForm()
    
    site_settings = SiteSettings.objects.first()
    context = {
        'form': form,
        'site_settings': site_settings,
        'yandex_maps_api_key': settings.YANDEX_MAPS_API_KEY,
    }
    return render(request, 'main/contact.html', context)
