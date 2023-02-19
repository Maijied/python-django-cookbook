from django.urls import path
from . import views

urlpatterns = {
    path('', views.counter, name='word_counter'),
    path('counter', views.counter, name='counter'),
}