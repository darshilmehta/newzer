from django.urls import path
from .views import search_news, NewsListView, NewsUSAListView, NewsAUSListView, NewsRussiaListView, NewsIndiaListView, NewsDetailView

urlpatterns = [
    path('all/', NewsListView.as_view(), name='home'),
    path('search/', search_news, name='search-news'),
    path('india/', NewsIndiaListView.as_view(), name='india'),
    path('usa/', NewsUSAListView.as_view(), name='usa'),
    path('australia/', NewsAUSListView.as_view(), name='australia'),
    path('russia/', NewsRussiaListView.as_view(), name='russia'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
]