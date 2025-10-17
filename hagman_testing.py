import tkinter as tk
from tkinter import messagebox
import random

WORDS = ["python", "coding", "variable", "hangman", "function", "loop", "inheritance"]

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x450")
        self.root.config(bg="#F3F4F6")

        self.header_frame = tk.Frame(self.root, bg="#2563EB", pady=10)
        self.header_frame.pack(fill="x")
        self.title_label = tk.Label(self.header_frame, text="HANGMAN GAME", font=("Arial", 20, "bold"), bg="#2563EB", fg="white")
        self.title_label.pack()

        self.settings_frame = tk.Frame(self.root, bg="#E5E7EB", pady=10)
        self.settings_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(self.settings_frame, text="Select Difficulty:", bg="#E5E7EB").grid(row=0, column=0, sticky="w")
        self.difficulty = tk.StringVar(value="medium")
        tk.Radiobutton(self.settings_frame, text="Easy", variable=self.difficulty, value="easy", bg="#E5E7EB").grid(row=0, column=1)
        tk.Radiobutton(self.settings_frame, text="Medium", variable=self.difficulty, value="medium", bg="#E5E7EB").grid(row=0, column=2)
        tk.Radiobutton(self.settings_frame, text="Hard", variable=self.difficulty, value="hard", bg="#E5E7EB").grid(row=0, column=3)
        self.sound_var = tk.BooleanVar()
        tk.Checkbutton(self.settings_frame, text="Enable Sound", variable=self.sound_var, bg="#E5E7EB").grid(row=1, column=0, columnspan=2, sticky="w")

        self.game_frame = tk.Frame(self.root, bg="#F3F4F6", pady=10)
        self.game_frame.pack(pady=10)
        self.word = random.choice(WORDS)
        self.display_word = ["_"] * len(self.word)
        self.guessed_letters = set()
        self.attempts = 6
        self.word_label = tk.Label(self.game_frame, text=" ".join(self.display_word), font=("Courier", 24, "bold"), bg="#F3F4F6", fg="#2563EB")
        self.word_label.pack(pady=10)
        self.info_label = tk.Label(self.game_frame, text=f"Attempts left: {self.attempts}", bg="#F3F4F6")
        self.info_label.pack()

        self.entry_frame = tk.Frame(self.root, bg="#F3F4F6")
        self.entry_frame.pack()
        tk.Label(self.entry_frame, text="Enter a letter:", bg="#F3F4F6").grid(row=0, column=0)
        self.letter_entry = tk.Entry(self.entry_frame, width=5, font=("Arial", 14))
        self.letter_entry.grid(row=0, column=1, padx=5)
        tk.Button(self.entry_frame, text="Guess", command=self.check_guess, bg="#2563EB", fg="white").grid(row=0, column=2, padx=5)

        self.control_frame = tk.Frame(self.root, bg="#E5E7EB", pady=10)
        self.control_frame.pack(fill="x", padx=10, pady=5)
        tk.Button(self.control_frame, text="Restart Game", bg="#10B981", fg="white", command=self.restart_game).pack(side="left", padx=20)
        tk.Button(self.control_frame, text="Exit", bg="#EF4444", fg="white", command=self.root.quit).pack(side="right", padx=20)

        # New section: show all possible words
        self.words_frame = tk.Frame(self.root, bg="#F3F4F6", pady=10)
        self.words_frame.pack(fill="x", padx=10, pady=5)
        tk.Label(self.words_frame, text="Possible Words:", font=("Arial", 10, "bold"), bg="#F3F4F6", fg="#111827").pack(anchor="w")
        tk.Label(self.words_frame, text=", ".join(WORDS), bg="#F3F4F6", fg="#374151", wraplength=580, justify="left").pack(anchor="w")

    def check_guess(self):
        guess = self.letter_entry.get().lower().strip()
        self.letter_entry.delete(0, tk.END)
        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid Input", "Please enter a single alphabet letter!")
            return
        if guess in self.guessed_letters:
            messagebox.showinfo("Info", "You already guessed that letter!")
            return
        self.guessed_letters.add(guess)
        if guess in self.word:
            for i, ch in enumerate(self.word):
                if ch == guess:
                    self.display_word[i] = guess
            self.word_label.config(text=" ".join(self.display_word))
            if "_" not in self.display_word:
                messagebox.showinfo("Congratulations!", f"You guessed the word '{self.word}'!")
                self.disable_game()
        else:
            self.attempts -= 1
            self.info_label.config(text=f"Attempts left: {self.attempts}")
            if self.attempts == 0:
                messagebox.showerror("Game Over", f"You lost! The word was '{self.word}'")
                self.disable_game()

    def restart_game(self):
        self.word = random.choice(WORDS)
        self.display_word = ["_"] * len(self.word)
        self.guessed_letters.clear()
        self.attempts = 6
        self.word_label.config(text=" ".join(self.display_word))
        self.info_label.config(text=f"Attempts left: {self.attempts}")
        self.letter_entry.config(state="normal")

    def disable_game(self):
        self.letter_entry.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
