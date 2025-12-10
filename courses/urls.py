from django.urls import path
from . import views
urlpatterns = [
    path('<slug:slug>/', views.course_detail, name='course_detail'),
    path('<slug:slug>/buy/', views.create_order, name='course_buy'),
    path('<slug:slug>/content/', views.course_content, name='course_content'),
    path('payment/success/', views.payment_success, name='payment_success'),
]
