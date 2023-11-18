from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('my_account/', views.my_account, name='my_account'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users.login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')

]
