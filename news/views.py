from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import ListView, DetailView


# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('title')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ""
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = "Error: Form was not valid"

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail.html'
    context_object_name = 'article'

# def detail(request):
#     return render(request, 'news/detail.html')