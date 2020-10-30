from phrasehunter.phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("Bazinga"),
            Phrase("Legendary"),
            Phrase("How you doin"),
            Phrase("Wubba Lubba Dub Dub"),
            Phrase("Ill be back"),
        ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f'Number missed {self.missed}')
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print("\n=========================")
        print("Welcome to Phrase Hunter")
        print("=========================\n")

    def get_guess(self):
        guess = input("\nGuess a letter  ")
        return guess

    def game_over(self):
        if self.missed == 5:
            print("You lost! Better luck next time.")
        else:
            print("You won the game!")
