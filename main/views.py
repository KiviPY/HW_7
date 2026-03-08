from django.shortcuts import render


# Create your views here.

def index(request):
    data = {'title': 'Main page',
            'values': ['Some', 'Hello', '123']} # для цикла for в html
    return render(request,'main/index.html', data)


def about(request):
    return render(request,'main/about.html')

def contacts(request):
    return render(request,'main/contacts.html')