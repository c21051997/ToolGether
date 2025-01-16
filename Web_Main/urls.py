from django.urls import path
from Web_Main import views

app_name = 'Web_Main'

urlpatterns = [
    path('', views.Home, name='index'),
    path('about/', views.About, name='about'),
    path('credits/', views.Credits, name='credits'),
    path('item/', views.Item, name='item'),
    path('search/', views.Search, name='search'),
]