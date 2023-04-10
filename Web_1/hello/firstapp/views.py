from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import UserForm
from .models import Person
from django.template.response import TemplateResponse


# def home(request):
#     userform = UserForm()
#     if request.method == "POST":
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data["name"]
#             return HttpResponse("<h2>Имя введено коррректно-{0}</h2>".format(name))
#     return render(request, "firstapp/index.html", {"form": userform})


def index(request):
    people = Person.objects.all()
    return render(request, "firstapp/index.html", {"people": people})
    # userform = UserForm
    # return render(request, "firstapp/index.html", {"form": userform})


def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "firstapp/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиeнт не найден</h2>")


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиeнт не найден</h2>")


# userform = UserForm
# person = {"age": 70}
# cat = ["Ноутбуки", "Принтеры", "Сканеры", "диски", "Шнуры"]
# data = {"cat": cat, "person": person, "form": userform}
# return render(request, 'firstapp/index.html', data)
# header = "Персональные данные"
# langs = ["Английский", "Турецкий", "Русский", "Кыргызский"]
# user = {"name": "Arsen,", "age": 20}
# addr = ("Талас", "Талас", "Темиркул", 48)
# data = {"header": header, "langs": langs, "user": user, "address": addr}
# # return render(request, "index.html", context=data)
# return TemplateResponse(request, "firstapp/index.html", data)


def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = "<h2>Пользователь</h2><h3>Имя: {0}, Возраст - {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, 'firstapp/index.html', {"form": userform})


def about(request):
    return HttpResponse('<h2>0 сайте<h2>')


def contact(request):
    return HttpResponseRedirect('/about')


def details(request):
    return HttpResponsePermanentRedirect('/')


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0}  Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Arsen")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)
