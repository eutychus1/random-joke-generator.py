import tkinter as tk
import random

# Jokes categorized
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

# GUI application
def show_joke(category):
    joke = random.choice(jokes[category])
    output_label.config(text=joke)

# Create main window
root = tk.Tk()
root.title("Python Joke Generator")
root.geometry("600x400")
root.config(bg="black")

# ASCII art display
ascii_label = tk.Label(
    root, text=ascii_art, font=("Courier", 9), fg="lightgreen", bg="black", justify="left"
)
ascii_label.pack(pady=10)

# Buttons for joke categories
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=5)

python_button = tk.Button(
    button_frame, text="Python Jokes 🐍", command=lambda: show_joke("Python"),
    bg="#306998", fg="white", font=("Arial", 12), padx=10, pady=5
)
python_button.grid(row=0, column=0, padx=10)

programming_button = tk.Button(
    button_frame, text="Programming Jokes 💻", command=lambda: show_joke("Programming"),
    bg="#444", fg="white", font=("Arial", 12), padx=10, pady=5
)
programming_button.grid(row=0, column=1, padx=10)

# Output label for joke
output_label = tk.Label(root, text="", wraplength=500, font=("Arial", 14), bg="black", fg="cyan")
output_label.pack(pady=30)

# Run the GUI loop
root.mainloop()
