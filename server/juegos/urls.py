from django.urls import path
from .views import GameDetailAPIView, GameCreateView

urlpatterns = [
    path('game-detail/<int:pk>/', GameDetailAPIView.as_view(), name='update_game'),
     
]
