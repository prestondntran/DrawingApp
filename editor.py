from tkinter import *

# initialize editor function
def initEditor(toolkit):
    global palette, selectedColor, currShape, selected
    # create palette
    defaultColors = ["#ff0000", "#ffa500", "#ffff00", "#00ff00", "#00ffff", "#0000ff", "#8f34eb", "#000000", "#ffffff"]
    palette = []
    for i in range(9):
        palette.append(toolkit.create_oval(30 + (50 * i), 315, 70 + (50 * i), 355, outline = "black", width = 2, tags = ('blackOutline')))
        toolkit.itemconfig(palette[i], fill = defaultColors[i])

    # display hex code for selected color
    selectedColor = toolkit.create_text(250, 300, text = "", font = ('Helvetica', '15', 'bold'), fill = "#868686")

    # tracks the selected shape or previously clicked shape
    currShape = palette[0]
    # tracks state of currShape
    selected = False

# color click function
def colorClick(shape, toolkit):
    global currShape, selected
    # change previous shape
    if ("blackOutline" in toolkit.itemcget(currShape, 'tags')):
        shapeOutline = "black"
    else:
        shapeOutline = ""
    toolkit.itemconfig(currShape, outline = shapeOutline)
    
    # click same shape
    if (shape == currShape):
        if (selected):
            toolkit.itemconfig(shape, outline = shapeOutline)
            selected = False
        else:
            toolkit.itemconfig(shape, outline = "#00aaff")
            selected = True
    # click different shape
    else:
        toolkit.itemconfig(shape, outline = "#00aaff")
        selected = True
    
    currShape = shape
    displayColor(shape, toolkit)

# color display function
def displayColor(shape, toolkit):
    if (selected):
        toolkit.itemconfig(selectedColor, text = "ID: " + toolkit.itemcget(shape, "fill").lower())
    else:
        toolkit.itemconfig(selectedColor, text = "")

# change palette function
def paletteChange(circle, toolkit):
    # check if palette should be changed (palette not selected)
    change = True
    for i in range(len(palette)):
        if (currShape == palette[i]):
            change = False

    if (change and selected):
        newColor = toolkit.itemcget(currShape, "fill")
        toolkit.itemconfig(circle, fill = newColor)
    colorClick(circle, toolkit)