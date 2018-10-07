from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
    path("", view=views.ChangePassword.as_view()),
    path("profile/<str:username>", view=views.Profile.as_view()),
]
