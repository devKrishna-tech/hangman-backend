from django.urls import path
from .views import NewGameView, GameStateView, GuessView

urlpatterns = [
    path('game/new', NewGameView.as_view(), name='new-game'),
    path('game/<int:game_id>', GameStateView.as_view(), name='game-state'),
    path('game/<int:game_id>/guess', GuessView.as_view(), name='game-guess'),
]
