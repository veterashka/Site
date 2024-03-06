from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app.models import ModelReg


@csrf_exempt
def index(request):
    if request.method == 'POST': pass
    return render(request, 'index.html')


user_info = {"": False}


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = ModelReg.objects.all()
        for i in data:
            if request.POST['email'] == i.email:
                return render(request, 'index.html', {"err": f'Email: {i.email} занят другим пользователем'})
        reg = ModelReg()
        reg.email = request.POST['email']
        reg.password = request.POST['password']
        reg.login = request.POST['login']
        reg.save()
        return HttpResponse(f'Пользователь с Email: {reg.email} успешно зарегистрирован!')
    return render(request, 'registration.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = ModelReg.objects.all()
        print(data)
        print(f"Из пост запроса. Почта: {request.POST['email']} Pass: {request.POST['password']}")
        for i in data:
            print(f'Текущий объект из базы данных. Почта: {i.email} Pass: {i.password}')
            if request.POST['email'] == i.email and request.POST['password'] == i.password:
                user_login = request.POST['email']
                user_info[user_login] = True
                html = redirect('/profile', {'user': user_login})
                html.set_cookie('isAuth', user_login)
                return html

        return render(request, 'index.html', {'err': 'авторизация не пройдена'})
    return render(request, 'login.html')


@csrf_exempt
def profile(request):
    if request.method == 'POST':
        html = redirect('/')
        html.delete_cookie('isAuth')
        return html
    r = ''
    try:
        r = request.COOKIES['isAuth']
    except:
        return redirect('/')
    return render(request, 'profile.html', {'user': request.COOKIES['isAuth']})


