import tkinter as tk
import string
import random
def generate_passcode():
    passcode= []
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        passcode.append(alpha)
        passcode.append(symbol)
        passcode.append(numbers)
        passwords = " ".join(str(x)for x in passcode)
        label.config(text=passwords)
root = tk.Tk()
root.geometry("400x300")
button = tk.Button(root, text="Generate Password", command=generate_passcode)
button.grid(row=1, column=1)
label = tk.Label(root, font=("times", 15, "bold"))
label.grid(row=4, column=2)
root.mainloop()
