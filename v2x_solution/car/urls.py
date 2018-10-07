from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.Cars.as_view(), name='cars'),
    path('criminalcars/', views.CriminalCars.as_view(), name='criminalcars'),
    path('postcars/', views.PostCars.as_view(), name='postcars'),
    path('postcars/<int:postcars_id>/', views.ModeratePostCars.as_view(), name='moderate_postcars')
]