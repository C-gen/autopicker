from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    """Форма для заявки на автоподбор"""
    
    class Meta:
        model = Application
        fields = ['name', 'phone', 'budget', 'brand_model', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (999) 123-45-67'
            }),
            'budget': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: 500 000 - 800 000 руб.'
            }),
            'brand_model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Toyota Camry, BMW X5'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Дополнительная информация о ваших пожеланиях'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Простая валидация телефона
        phone = ''.join(filter(str.isdigit, phone))
        if len(phone) < 10:
            raise forms.ValidationError('Введите корректный номер телефона')
        return phone


class ContactForm(forms.Form):
    """Форма для обратной связи"""
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше имя'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your@email.com'
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Тема сообщения'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Ваше сообщение'
        })
    ) 