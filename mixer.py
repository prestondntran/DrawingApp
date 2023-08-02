from tkinter import *
from tkinter import messagebox
import matplotlib

# initialize mixer function
def initMixer(root, toolkit):
    global hexInput1, hexInput2, colorButton1, colorButton2, colorOutput1, colorOutput2, spectrumBorder, spectrum
    hexInput1 = Entry(root, width = 15)
    hexInput1.insert(0, "#ffffff")

    hexInput2 = Entry(root, width = 15)
    hexInput2.insert(0, "#ffffff")

    colorButton1 = Button(root, text = "Create")
    colorButton2 = Button(root, text = "Create")

    colorOutput1 = toolkit.create_oval(70, 85, 170, 185, outline = "black", fill = "#ffffff", width = 2, state = "hidden", tags = ('blackOutline'))
    colorOutput2 = toolkit.create_oval(320, 85, 420, 185, outline = "black", fill = "#ffffff", width = 2, state = "hidden", tags = ('blackOutline'))

    spectrumBorder = toolkit.create_rectangle(30, 225, 470, 275, outline = "black", width = 3, state = "hidden")
    spectrum = []
    for i in range(20):
        spectrum.append(toolkit.create_rectangle(30 + (22 * i), 225, 52 + (22 * i), 275, outline = "", fill = "#ffffff", width = 2, state = "hidden"))

# show mixer function
def showMixer(toolkit):
    hexInput1.place(x = 55, y = 10)
    hexInput2.place(x = 305, y = 10)
    colorButton1.place(x = 82, y = 40)
    colorButton2.place(x = 332, y = 40)
    toolkit.itemconfig(colorOutput1, state = "normal")
    toolkit.itemconfig(colorOutput2, state = "normal")
    toolkit.itemconfig(spectrumBorder, state = "normal")
    for i in range(len(spectrum)):
        toolkit.itemconfig(spectrum[i], state = "normal")

# hide mixer function
def hideMixer(toolkit):
    hexInput1.place_forget()
    hexInput2.place_forget()
    colorButton1.place_forget()
    colorButton2.place_forget()
    toolkit.itemconfig(colorOutput1, state = "hidden")
    toolkit.itemconfig(colorOutput2, state = "hidden")
    toolkit.itemconfig(spectrumBorder, state = "hidden")
    for i in range(len(spectrum)):
        toolkit.itemconfig(spectrum[i], state = "hidden")

# spectrum change function
def setSpectrum(toolkit):
    # get spectrum end codes
    hex1 = hexInput1.get()
    hex2 = hexInput2.get()
    if (hex1[0] != "#"):
        try:
            hex1 = matplotlib.colors.cnames[hex1.lower()]
        except KeyError:
            return
    else:
        if (len(hex1) != 7):
            return
    if (hex2[0] != "#"):
        try:
            hex2 = matplotlib.colors.cnames[hex2.lower()]
        except KeyError:
            return
    else:
        if (len(hex1) != 7):
            return

    # set spectrum ends
    try:
        toolkit.itemconfig(spectrum[0], fill = hex1)
        toolkit.itemconfig(spectrum[len(spectrum) - 1], fill = hex2)
    except TclError:
        return

    # rgb arrays hold red, green, and blue values of hex codes
    # transform is how much to increment red, green, and blue
    rgb1 = []
    rgb2 = []
    transform = []
    for i in range(3):
        rgb1.append(int(hex1[(1+2*i):(3+2*i)], 16))
        rgb2.append(int(hex2[(1+2*i):(3+2*i)], 16))
        transform.append(abs(rgb1[i] - rgb2[i]) / float(len(spectrum) - 1))

    # set colors of spectrum
    for i in range(1, len(spectrum) - 1):
        newHex = "#"
        for j in range(3):
            # if first color is greater, lessen color by subtracting
            if (rgb1[j] > rgb2[j]):
                transform[j] *= -1

            # add hex code segment to newHex
            subColor = hex(int(rgb1[j] + (transform[j] * i)))
            if (len(subColor) < 4):
                subColor = subColor[:2] + "0" + subColor[2:]
            newHex += subColor[2:]
            
            # change transform back to positive
            if (rgb1[j] > rgb2[j]):
                transform[j] *= -1
        toolkit.itemconfig(spectrum[i], fill = newHex)