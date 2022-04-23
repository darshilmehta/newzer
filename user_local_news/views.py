from .models import LocalNews
from .forms import LocalNewsForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def get_local_news(request):
    if request.method == 'POST':
       form = LocalNewsForm(request.POST)
       if form.is_valid():
            name = request.POST.get('name')
            title = request.POST.get('title')
            content = request.POST.get('content')
            image_url = request.POST.get('image_url')
            country_name = request.POST.get('country_name')
            local_news = LocalNews(
               name=name,
               country_name=country_name,
               title=title,
               content=content,
               image_url=image_url,
               is_authenticated=False)
            local_news.save()
            messages.success(request, 'We have submitted your news for verification. Thankyou for your contribution!')
            return redirect('local-home')
    else:
        form = LocalNewsForm()
    return render(request, 'user_local_news/post_local_news.html', {'form': form})

class LocalNewsListView(ListView):
    model = LocalNews
    template_name = 'user_local_news/localnews.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        filter_val = True
        new_context = LocalNews.objects.filter(
            is_authenticated=filter_val,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(LocalNewsListView, self).get_context_data(**kwargs)
        context['filter'] = True
        return context

class LocalNewsDetailView(LoginRequiredMixin, DetailView):
    model = LocalNews
