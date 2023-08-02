from tkinter import *
import editor

# initialize artist function
def initArtist(root):
    global mode, penMode, clearButton, sizeScale
    
    mode = StringVar()
    mode.set("Pen")
    penMode = OptionMenu(root, mode, "Pen", "Line", "Circle", "Square", "Triangle", "Eraser", command = lineMode)
    penMode.config(width = 15)
    penMode.place(x = 210, y = 360)

    clearButton = Button(root, text = "Clear")
    clearButton.place(x = 350, y = 360)

    sizeScale = Scale(root, from_ = 1, to = 50, orient = HORIZONTAL, length = 200)
    sizeScale.place(x = 150, y = 390)

# stamping function (click canvas)
def stamp(event, toolkit, canvas):
    global x, y, line
    x, y = event.x, event.y
    # set pen color and size
    penColor = ""
    penSize = sizeScale.get()
    if (editor.selected):
        penColor = toolkit.itemcget(editor.currShape, "fill")

    # draws based on mode selected
    if (penColor != ""):
        if (mode.get() == "Eraser" or mode.get() == "Pen"):
            draw(event, toolkit, canvas)
        elif (mode.get() == "Circle"):
            canvas.create_oval(x-penSize, y-penSize, x+penSize, y+penSize, fill = penColor, outline = penColor)
        elif (mode.get() == "Square"):
            canvas.create_rectangle(x-penSize, y-penSize, x+penSize, y+penSize, fill = penColor, outline = penColor)
        elif (mode.get() == "Triangle"):
            canvas.create_polygon(x, y-penSize, x-penSize, y+penSize, x+penSize, y+penSize, fill = penColor, outline = penColor)
        elif (mode.get() == "Line"):
            if (line[0] == True):
                canvas.create_line(x, y, line[1], line[2], fill = penColor, width = penSize, capstyle = "round")
                line = [False]
            else:
                canvas.create_line(x, y, event.x, event.y, fill = penColor, width = penSize, capstyle = "round")
                line = [True, x, y]


# drawing function
def draw(event, toolkit, canvas):
    global x, y
    # set pen color and size
    penColor = ""
    penSize = sizeScale.get()
    if (editor.selected and mode.get() == "Pen"):
        penColor = toolkit.itemcget(editor.currShape, "fill")

    if (mode.get() == "Eraser"):
        penColor = "#ffffff"
        penSize = 25

    if (penColor != ""):
        canvas.create_line(x, y, event.x, event.y, fill = penColor, width = penSize, capstyle = "round")
    x, y = event.x, event.y

# line status function
def lineMode(event):
    global line
    # line holds boolean that tracks whether to draw line as well as previous x and y values
    line = [False]