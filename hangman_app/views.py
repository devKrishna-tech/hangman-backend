from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Game
from .serializers import GameSerializer

class NewGameView(APIView):
    def post(self, request):
        game = Game.create_new_game()
        return Response({'id': game.id}, status=status.HTTP_201_CREATED)

class GameStateView(APIView):
    def get(self, request, game_id):
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GameSerializer(game)
        return Response(serializer.data)

class GuessView(APIView):
    def post(self, request, game_id):
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        letter = request.data.get('letter', '').lower()
        if not letter or len(letter) != 1 or not letter.isalpha():
            return Response({'error': 'Invalid letter'}, status=status.HTTP_400_BAD_REQUEST)

        correct = game.make_guess(letter)
        serializer = GameSerializer(game)
        return Response({'correct': correct, **serializer.data})
