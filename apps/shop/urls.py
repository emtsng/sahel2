from django.urls import path

from apps.shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('<int:pk>/', views.product_detail, name='detail'),
]
