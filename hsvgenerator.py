from tkinter import *
import colorsys

# initialize hsv generator function
def initHSVGenerator(root, toolkit):
    global colorOutput, hue, saturation, value, hLabel, sLabel, vLabel
    colorOutput = toolkit.create_oval(200, 185, 300, 285, outline = "black", fill = "#ffffff", width = 2, state = "hidden", tags = ('blackOutline'))
    
    hue = Scale(root, from_ = 0, to = 360, orient = HORIZONTAL, length = 300)
    saturation = Scale(root, from_ = 0, to = 100, orient = HORIZONTAL, length = 300)
    value = Scale(root, from_ = 0, to = 100, orient = HORIZONTAL, length = 300)
    saturation.set(100)
    value.set(100)

    hLabel = toolkit.create_text(90, 50, text = "H", font = ('Helvetica', '15', 'bold'), state = "hidden")
    sLabel = toolkit.create_text(90, 100, text = "S", font = ('Helvetica', '15', 'bold'), state = "hidden")
    vLabel = toolkit.create_text(90, 150, text = "V", font = ('Helvetica', '15', 'bold'), state = "hidden")

# show hsv generator function
def showHSVGenerator(toolkit):
    global selected
    toolkit.itemconfig(colorOutput, state = "normal")
    hue.place(x = 100, y = 25)
    saturation.place(x = 100, y = 75)
    value.place(x = 100, y = 125)
    toolkit.itemconfig(hLabel, state = "normal")
    toolkit.itemconfig(sLabel, state = "normal")
    toolkit.itemconfig(vLabel, state = "normal")

# hide hsv generator function
def hideHSVGenerator(toolkit):
    toolkit.itemconfig(colorOutput, state = "hidden")
    hue.place_forget()
    saturation.place_forget()
    value.place_forget()
    toolkit.itemconfig(hLabel, state = "hidden")
    toolkit.itemconfig(sLabel, state = "hidden")
    toolkit.itemconfig(vLabel, state = "hidden")

# update color function
def updateColor(toolkit):
    h = hue.get() / float(360)
    s = saturation.get() / float(100)
    v = value.get() / float(100)
    (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
    (r, g, b) = (int(r * 255), int(g * 255), int(b * 255))
    hexCode = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    toolkit.itemconfig(colorOutput, fill = hexCode)