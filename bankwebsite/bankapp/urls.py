from . import views
from django.urls import path

app_name='bankapp'
urlpatterns = [

    path('', views.home, name='home'),
    path('main',views.home,name='loghome'),
    path('entry', views.form_page, name='form'),


]