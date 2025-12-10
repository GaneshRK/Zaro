from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/login/', views.login_register, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
