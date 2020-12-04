from .models import Register
from django.forms import ModelForm,TextInput, DateTimeInput,Textarea

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ('title', 'name', 'date', 'time')

widgets = {

"title": TextInput (attrs={
    'class': 'form-control',
    'placeholder': 'Процедура'
}),

"name": TextInput (attrs={
    'class': 'form-control',
    'placeholder': 'Процедура'
}),
"date": DateTimeInput (attrs={
    'class': 'form-control',
             'placeholder': 'Дата'

}),
"time": TextInput (attrs={
    'class': 'form-control',
    'placeholder': 'Время'

}),
}