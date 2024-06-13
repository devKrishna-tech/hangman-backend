from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    display_word = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'state', 'incorrect_guesses', 'max_incorrect_guesses', 'display_word']

    def get_display_word(self, obj):
        return obj.get_display_word()
