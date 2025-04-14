import tkinter as tk
from math import sqrt, sin, cos, tan, radians

# Function to handle button click
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screen_var.get())
            screen_var.set(value)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")  # Clear the display
    else:
        screen_var.set(screen_var.get() + text)
    screen.update()

# Function for square root operation
def square_root():
    try:
        value = sqrt(float(screen_var.get()))
        screen_var.set(value)
    except ValueError:
        screen_var.set("Error")
    screen.update()

# Function for trigonometric operations
def sine():
    try:
        angle = radians(float(screen_var.get()))  # Convert degrees to radians
        result = sin(angle)
        screen_var.set(result)
    except ValueError:
        screen_var.set("Error")
    screen.update()

def cosine():
    try:
        angle = radians(float(screen_var.get()))  # Convert degrees to radians
        result = cos(angle)
        screen_var.set(result)
    except ValueError:
        screen_var.set("Error")
    screen.update()

def tangent():
    try:
        angle = radians(float(screen_var.get()))  # Convert degrees to radians
        result = tan(angle)
        screen_var.set(result)
    except ValueError:
        screen_var.set("Error")
    screen.update()

# Main window setup
root = tk.Tk()
root.geometry("400x600")
root.title("Python GUI Calculator")

# Set background color of the window
root.config(bg="lightblue")

# Entry widget for the calculator display with background color
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", bd=10, insertwidth=4, width=14, borderwidth=4, bg="lightyellow")
screen.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

# Frame to hold buttons
buttons_frame = tk.Frame(root, bg="lightblue")
buttons_frame.pack()

# Create buttons with background colors
buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', 'sqrt',
    '1', '2', '3', '-', 'sin',
    '0', '.', '=', '+', 'cos'
]

i = 0
for button in buttons:
    btn_color = "lightgray" if button.isdigit() or button == '.' else "lightgreen"
    btn = tk.Button(buttons_frame, text=button, font="Arial 18 bold", padx=10, pady=10, bg=btn_color)
    btn.grid(row=i//5, column=i%5, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    if button == 'sqrt':
        btn.config(command=square_root)
    elif button == 'sin':
        btn.config(command=sine)
    elif button == 'cos':
        btn.config(command=cosine)
    elif button == 'tan':
        btn.config(command=tangent)
    i += 1

# Start the Tkinter loop
root.mainloop()
