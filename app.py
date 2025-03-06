# PROJECT: 5
# HAGMAN GAME PROJECT

import random

words = ["python", "javascript", "java", "php", "ruby"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to the Hangman Game! 🏆")
print("🔍 Try to guess the word letter by letter.")
print("_ " * len(word))  

while attempts > 0:
    guess = input("\n🔠 Guess a Letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter Only One Alphabet!")
        continue
    if guess in guessed_letters:
        print("🔁 You've already guessed this letter! Try another one.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess! 🎉")
    else:
        attempts -= 1
        print(f"❌ Wrong Guess! {attempts} attempts left. 💔")

    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(display_word)

    if "_" not in display_word:
        print(f"🎊 Congratulations! 🎉 You Won! The Correct Word Was: {word.upper()} 🏆")
        break

else:
    print("💀 Game Over! 😢")
    print(f"🔤 The Correct Word Was: {word.upper()}")
