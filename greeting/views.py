from django.shortcuts import render
from .models import Email


def index(request):
    title = 'Главная'
    return render(request, 'greeting/index.html', {'title': title})


def hello(request):
    title = 'Приветствие'
    context = {
        'title': title,
    }
    if request.method == 'POST':
        new_email = request.POST['email'].lower()
        email = Email.objects.filter(email=new_email)
        if not email:
            Email.objects.create(email=new_email)
            hello_str = 'Привет, ' + new_email
            context['data'] = hello_str
        else:
            hello_str = 'Уже виделись, ' + str(email[0])
            context['data'] = hello_str
        return render(request, 'greeting/hello.html', context=context)


def list(request):
    title = 'С кем уже здоровались'
    users = Email.objects.all()
    context = {
        'title': title,
        'users': users,
        'count': len(users)
    }
    return render(request, 'greeting/list.html', context=context)


def about(request):
    context = {
        'title': 'О сайте'
    }
    return render(request, 'greeting/about.html', context=context)
