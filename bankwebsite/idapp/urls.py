from . import views
from django.urls import path

app_name='idapp'
urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),

]