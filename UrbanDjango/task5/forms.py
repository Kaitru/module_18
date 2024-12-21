from django import forms

class sign_up_by_django(forms.Form):
    users = ['Антон', 'Дмитрий', 'Александр', 'Денис']
    info = {}
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(label='Повторите пароль')
    age = forms.CharField(label='Введите возраст')
