from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.Events.as_view(), name='events'),
    path('<int:event_id>', views.ModerateEvent.as_view(), name='moderate_events'),
    path('search/', views.Search.as_view(), name='Search'),
]