
from app_site_terapeuta import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('whatsapp/', views.whatsapp, name='whatsapp'),
    path('obrigado/', views.obrigado, name='obrigado'),
    path('instagram/', views.instagram, name='instagram'),
]
