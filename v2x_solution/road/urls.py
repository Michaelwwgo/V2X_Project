from django.urls import path
from . import views

app_name = 'roads'

urlpatterns = [
    path('', views.Roads.as_view(), name='roads'),
    path('situation/<int:situation_id>', views.ModerateSituation.as_view(), name='moderate_situation'),
    path('situation/search/', views.Search.as_view(), name='Search'),
    path('situation/', views.Situations.as_view(), name='situation'),
]