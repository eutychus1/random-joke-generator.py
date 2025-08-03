import tkinter as tk
import random
import pygame

# Initialize sound
pygame.mixer.init()
try:
    pygame.mixer.music.load("rimshot.mp3")  # Make sure this file is in the same directory
except pygame.error:
    print("Sound file not found. Add 'rimshot.mp3' to your folder.")

# Joke categories
jokes = {
    "Python": [
        "Why do Python programmers wear glasses? Because they can't C!",
        "Why did the Python programmer get kicked out of school? Because he kept importing random.",
        "Why does Python live on land? Because it’s above C level!",
        "In Python, indentationError is never funny... unless you're writing a joke with it!"
    ],
    "Programming": [
        "Why did the developer go broke? Because he used up all his cache.",
        "I just saw my life flash before my eyes. It was a segfault.",
        "There are 10 types of people: those who understand binary and those who don't.",
        "How many programmers does it take to change a light bulb? None. That’s a hardware problem.",
        "I would tell you a joke about recursion, but you'd have to understand recursion to get it."
    ]
}

# ASCII art title
ascii_art = r"""
    ____       _   _                 _                 
   |  _ \ __ _| |_| |__   ___   ___ | | ___   __ _ ___ 
   | |_) / _` | __| '_ \ / _ \ / _ \| |/ _ \ / _` / __|
   |  __/ (_| | |_| | | | (_) | (_) | | (_) | (_| \__ \
   |_|   \__,_|\__|_| |_|\___/ \___/|_|\___/ \__, |___/
                                              |___/    
             🤓 Welcome to the Code Joke Hub! 🐍
"""

# Background colors to cycle through
bg_colors = ["#1c1c1c", "#222244", "#2c3e50", "#3d3d3d", "#004d40", "#0f3057", "#212121", "#001f3f"]
text_colors = ["#00ffff", "#00ffcc", "#ffcc00", "#ff4081", "#7CFC00", "#ffffff"]

# Play sound
def play_sound():
    try:
        pygame.mixer.music.play()
    except:
        pass

# Show joke from category
def show_joke(category):
    joke = random.choice(jokes[category])
    output_label.config(text=joke)
    play_sound()

# Show random joke
def show_random_joke():
    category = random.choice(list(jokes.keys()))
    show_joke(category)

# Cycle background color
def change_background():
    new_bg = random.choice(bg_colors)
    new_fg = random.choice(text_colors)

    root.config(bg=new_bg)
    ascii_label.config(bg=new_bg, fg=new_fg)
    output_label.config(bg=new_bg, fg=new_fg)
    button_frame.config(bg=new_bg)

    for widget in button_frame.winfo_children():
        widget.config(bg="#333", fg="white")

    root.after(4000, change_background)  # Change every 4 seconds

# GUI setup
root = tk.Tk()
root.title("Python Joke Generator")
root.geometry("650x500")
root.config(bg="black")

# ASCII art label
ascii_label = tk.Label(
    root, text=ascii_art, font=("Courier", 9), fg="lightgreen", bg="black", justify="left"
)
ascii_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=5)

tk.Button(button_frame, text="Python Jokes 🐍", command=lambda: show_joke("Python"),
          bg="#306998", fg="white", font=("Arial", 12), padx=10, pady=5).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Programming Jokes 💻", command=lambda: show_joke("Programming"),
          bg="#444", fg="white", font=("Arial", 12), padx=10, pady=5).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="New Random Joke 🔁", command=show_random_joke,
          bg="#00a86b", fg="white", font=("Arial", 12), padx=10, pady=5).grid(row=0, column=2, padx=10)

# Output label
output_label = tk.Label(root, text="", wraplength=600, font=("Arial", 14), bg="black", fg="cyan", justify="center")
output_label.pack(pady=30)

# Start color cycling
change_background()

# Run app
root.mainloop()
