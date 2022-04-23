from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm
from .models import News
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
       form = UserRegisterationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Account created for {username}! Please Login now.')
           return redirect('login')
    else:
        form = UserRegisterationForm()
    return render(request, 'news/register.html', {'form': form})

@login_required
def about(request):
    return render(request, 'news/about.html')

@login_required
def search_news(request):
    if request.method == "POST":
        searched = request.POST['searched']
        news = News.objects.filter(title__icontains = searched)
        content = {
            'searched': searched,
            'all_news': news,
            'totalbooks': news.count
        }
        return render(request, 'news/news_search.html', content)
    else:
        content = {
            'searched': False
        }
        return render(request, 'news/news_search.html', content)


class NewsListView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news/news_basic.html'
    context_object_name = 'all_news'

class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News

class NewsIndiaListView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news/news_basic.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        filter_val = "India"
        new_context = News.objects.filter(
            country_name=filter_val,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(NewsIndiaListView, self).get_context_data(**kwargs)
        context['filter'] = "India"
        return context

class NewsAUSListView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news/news_basic.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        filter_val = "Australia"
        new_context = News.objects.filter(
            country_name=filter_val,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(NewsAUSListView, self).get_context_data(**kwargs)
        context['filter'] = "Australia"
        return context

class NewsUSAListView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news/news_basic.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        filter_val = "USA"
        new_context = News.objects.filter(
            country_name=filter_val,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(NewsUSAListView, self).get_context_data(**kwargs)
        context['filter'] = "USA"
        return context

class NewsRussiaListView(LoginRequiredMixin, ListView):
    model = News
    template_name = 'news/news_basic.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        filter_val = "Russia"
        new_context = News.objects.filter(
            country_name=filter_val,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(NewsRussiaListView, self).get_context_data(**kwargs)
        context['filter'] = "Russia"
        return context