from django.urls import path
from greeting.views import index, list, hello, about

urlpatterns = [
    path('', index, name='index'),
    path('list/', list, name='list'),
    path('hello/', hello, name='hello'),
    path('about/', about, name='about'),
]