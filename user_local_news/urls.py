from django.urls import path
from .views import get_local_news, LocalNewsListView, LocalNewsDetailView

urlpatterns = [
    path('all/', LocalNewsListView.as_view(), name='local-home'),
    path('post-local-news/', get_local_news, name='post-local-news'),
    path('<int:pk>/', LocalNewsDetailView.as_view(), name='local-news-detail'),
]
