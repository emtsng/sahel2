from django.urls import path

from apps.services import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='list'),
    path('<int:pk>/', views.service_detail, name='detail'),
]
