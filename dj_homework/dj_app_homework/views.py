from django.shortcuts import render
from django.http import *
from .forms import *
from .models import *

# Create your views here.


# Method main page.
def index(request):
    if request.method == "GET":
        form = UserForm
        people = RegistrationPerson.objects.all()
        return render(request, "index.html", {"form": form, "people": people})

    # Сохранение данных в БД.
    if request.method == "POST":
        form = UserForm
        # Выводим форму на экран в PyCharm обычным принтом.
        login = request.POST.get("login")
        password = request.POST.get("password")
        age = request.POST.get('age')
        print(f"\n{login=}, \n{password=}, \n{age=}")

        # Способ поинтереснее :)
        people = RegistrationPerson.objects.all()
        client = RegistrationPerson()
        client.login = request.POST.get("login")
        client.password = request.POST.get("password")
        client.age = request.POST.get("age")
        client.save()
        print(f"Логин: {client.login} \nПароль: {client.password} \nВозраст: {client.age}")
        return render(request, "index.html", {"form": form, "people": people, "login": login})
        # return HttpResponse(f"Логин: {login} <br> Пароль: {password}")


# Изменения в базе данных.
def edit(request, id_people):
    try:
        people = RegistrationPerson.objects.get(name=id_people)
    except RegistrationPerson.objects.DoesNotExist:
        return HttpResponseNotFound("<h2>Логин не найден.</h2>")


# Удаление данных из базы данных.
def delete(request, id):
    try:
        client = RegistrationPerson.objects.get(id=id)
        client.delete()
        print(f"Клиент с логином: {client.login} удалён из базы данных.")
        return HttpResponseRedirect('/')
    except RegistrationPerson.objects.DoesNotExist:
        return HttpResponseNotFound("<h1>Нет такого логина</h1>")
