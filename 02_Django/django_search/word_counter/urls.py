from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='word_counter_index'),
    path('counter/', views.counter, name='counter'),
    path('counter_post', views.counter_post, name='counter_post'),
}
