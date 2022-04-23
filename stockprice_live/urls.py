from django.urls import path
from .views import all_stocks, indian_stocks, global_stocks, crypto_currency

urlpatterns = [
    path('all-stocks/', all_stocks, name='all-stocks'),
    path('india/', indian_stocks, name='indian-stocks'),
    path('global/', global_stocks, name='global-stocks'),
    path('crypto-currency/', crypto_currency, name='crypto-currency'),
]
