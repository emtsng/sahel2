from django.urls import path

from apps.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]
