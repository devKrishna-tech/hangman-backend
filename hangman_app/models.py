from django.db import models
import random

WORD_LIST = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]

class Game(models.Model):
    word = models.CharField(max_length=100)
    state = models.CharField(max_length=10, default="InProgress")
    incorrect_guesses = models.IntegerField(default=0)
    max_incorrect_guesses = models.IntegerField()
    guessed_letters = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.word

    @staticmethod
    def create_new_game():
        word = random.choice(WORD_LIST).lower()
        max_incorrect_guesses = len(word) / 2
        return Game.objects.create(word=word, max_incorrect_guesses=max_incorrect_guesses)

    def get_display_word(self):
        return ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def make_guess(self, letter):
        if self.state != "InProgress":
            return

        letter = letter.lower()
        if letter in self.guessed_letters:
            return False
        
        self.guessed_letters += letter

        if letter not in self.word:
            self.incorrect_guesses += 1

        if all(l in self.guessed_letters for l in self.word):
            self.state = "Won"
        elif self.incorrect_guesses > self.max_incorrect_guesses:
            self.state = "Lost"

        self.save()
        return letter in self.word
