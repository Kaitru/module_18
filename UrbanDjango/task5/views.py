from django.contrib.auth import user_logged_in
from django.shortcuts import render
from django.http import HttpResponse
from .forms import sign_up_by_django as SignUpForm

# Create your views here.
def sign_up_by_html(request):
    users = ['Антон', 'Дмитрий', 'Александр', 'Денис']
    info = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            users.append(username)
            info['success'] = f'Приветствуем, {username}'

    return render(request, 'registration_page.html', info)

def sign_up_by_django(request):
    users = ['Антон', 'Дмитрий', 'Александр', 'Денис']
    info = {}
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                users.append(username)
                info['success'] = f'Приветствуем, {username}'
    else:
        form = SignUpForm()
    
    info['form'] = form
    return render(request, 'registration_page.html', info)