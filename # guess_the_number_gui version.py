# guess_the_number_gui.py

import random
import tkinter as tk
from tkinter import messagebox

class GuessTheNumberGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Guess the Number")
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 5

        self.guess_label = tk.Label(self.root, text="Enter your guess (1-100):")
        self.guess_label.pack(padx=10, pady=10)
        self.guess_entry = tk.Entry(self.root, width=20)
        self.guess_entry.pack(padx=10, pady=10)
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack(padx=10, pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(padx=10, pady=10)

    def check_guess(self):
        guess = int(self.guess_entry.get())

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text="Congratulations! You guessed the number.")
            self.guess_button.config(state="disabled")

        self.attempts -= 1
        if self.attempts == 0:
            self.result_label.config(text=f"Game over! The number was {self.number_to_guess}.")
            self.guess_button.config(state="disabled")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = GuessTheNumberGUI()
    gui.run()