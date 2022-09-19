
from django.contrib import admin
from django.urls import path , re_path



from home import views

urlpatterns = [
    path('',views.index , name='home'),
    path('services', views.services, name='services'),
    path('home', views.home, name='home'),
    path('form', views.form, name='form'),
    path('dataset', views.dataset, name='dataset'),
    path('model', views.model, name='model'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    re_path('predict',views.predict , name='predict')
]
 