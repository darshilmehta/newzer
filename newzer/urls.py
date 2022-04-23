from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from news import views as news_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', news_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='news/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='news/logout.html'), name='logout'),
    path('about/', news_views.about, name='about'),
    path('news/', include('news.urls')),
    path('local-news/', include('user_local_news.urls')),
    path('live-stock/', include('stockprice_live.urls')),
]