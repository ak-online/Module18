from django.shortcuts import render
from .forms import UserRegister

users = ['user_1', 'user_2', 'user_3']

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age<18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'registration_page.html', {'form': form, 'info': f"Приветствуем, {username}!"})
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info.get('error')})

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'registration_page.html', {'form': form, 'info': f"Приветствуем, {username}!"})
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info.get('error')})