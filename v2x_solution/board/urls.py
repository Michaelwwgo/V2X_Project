from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.AllBoard.as_view(), name='all_board'),
    path('<int:board_id>', views.Board.as_view(), name='board'),
    path('comment/<int:board_id>', views.Comment.as_view(), name='comment'),
]