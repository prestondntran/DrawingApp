from tkinter import *
from tkinter import messagebox
import matplotlib

# initialize generator function
def initGenerator(root, toolkit):
    global hexInput, colorButton, colorOutput
    hexInput = Entry(root, width = 15)
    hexInput.insert(0, "#ffffff")
    colorButton = Button(root, text = "Create")
    colorOutput = toolkit.create_oval(200, 150, 300, 250, outline = "black", fill = "#ffffff", width = 2, state = "hidden", tags = ('blackOutline'))

# show generator function
def showGenerator(toolkit):
    hexInput.place(x = 185, y = 75)
    colorButton.place(x = 212, y = 115)
    toolkit.itemconfig(colorOutput, state = "normal")

# hide generator function
def hideGenerator(toolkit):
    hexInput.place_forget()
    colorButton.place_forget()
    toolkit.itemconfig(colorOutput, state = "hidden")

# color change function
def setColor(toolkit, hexInput, colorOutput):
    # get hex code from input field
    hexCode = hexInput.get()

    # convert to matplotlib.colors
    if (hexCode[0] != "#"):
        try:
            hexCode = matplotlib.colors.cnames[hexCode.lower()]
        except KeyError:
            messagebox.showinfo("Invalid input", "Invalid input!")
            return
    else:
        if (len(hexCode) != 7):
            messagebox.showinfo("Invalid input", "Invalid input!")
            return

    # check for invalid input (color output)
    try:
        toolkit.itemconfig(colorOutput, fill = hexCode)
    except TclError:
        messagebox.showinfo("Invalid input", "Invalid input!")