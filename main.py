from tkinter import *
import generator, hsvgenerator, mixer, editor, artist

# set up GUI
root = Tk()
root.title("Drawing App")
root.geometry("500x900")
toolkit = Canvas(root, height = 400, width = 500)
canvas = Canvas(root, height = 400, width = 500, highlightbackground = "black", highlightthickness = 2)
toolkit.place(x = 0, y = 0)
canvas.place(x = 0, y = 430)

# set up artist tools
generator.initGenerator(root, toolkit)
hsvgenerator.initHSVGenerator(root, toolkit)
mixer.initMixer(root, toolkit)
editor.initEditor(toolkit)
artist.initArtist(root)

# toolkit option menu
mode = StringVar()
mode.set("Generator")
generator.showGenerator(toolkit)
def modeChange(event):
    if (mode.get() == "Generator"):
        # turn on appropriate mode, turn off others
        generator.showGenerator(toolkit)
        hsvgenerator.hideHSVGenerator(toolkit)
        mixer.hideMixer(toolkit)

        # deselect color when switching modes
        editor.selected = True
        editor.colorClick(editor.currShape, toolkit)
        editor.selected = False
        editor.displayColor(editor.currShape, toolkit)
    elif (mode.get() == "HSV Generator"):
        # turn on appropriate mode, turn off others
        generator.hideGenerator(toolkit)
        hsvgenerator.showHSVGenerator(toolkit)
        mixer.hideMixer(toolkit)

        # deselect color when switching modes
        editor.selected = True
        editor.colorClick(editor.currShape, toolkit)
        editor.selected = False
        editor.displayColor(editor.currShape, toolkit)
    else:
        # turn on appropriate mode, turn off others
        generator.hideGenerator(toolkit)
        hsvgenerator.hideHSVGenerator(toolkit)
        mixer.showMixer(toolkit)

        # deselect color when switching modes
        editor.selected = True
        editor.colorClick(editor.currShape, toolkit)
        editor.selected = False
        editor.displayColor(editor.currShape, toolkit)
toolkitMode = OptionMenu(toolkit, mode, "Generator", "HSV Generator", "Mixer", command = modeChange)
toolkitMode.config(width = 15)
toolkitMode.place(x = 70, y = 360)
    
# canvas binds
canvas.bind("<Button-1>", lambda event: artist.stamp(event, toolkit, canvas))
canvas.bind("<B1-Motion>", lambda event: artist.draw(event, toolkit, canvas))

# scale binds
hsvgenerator.hue.bind("<B1-Motion>", lambda _: [hsvgenerator.updateColor(toolkit), editor.displayColor(editor.currShape, toolkit)])
hsvgenerator.saturation.bind("<B1-Motion>", lambda _: [hsvgenerator.updateColor(toolkit), editor.displayColor(editor.currShape, toolkit)])
hsvgenerator.value.bind("<B1-Motion>", lambda _: [hsvgenerator.updateColor(toolkit), editor.displayColor(editor.currShape, toolkit)])

# button configurations
generator.colorButton.configure(command = lambda: [generator.setColor(toolkit, generator.hexInput, generator.colorOutput), editor.displayColor(editor.currShape, toolkit)])
mixer.colorButton1.configure(command = lambda: [generator.setColor(toolkit, mixer.hexInput1, mixer.colorOutput1), mixer.setSpectrum(toolkit), editor.displayColor(editor.currShape, toolkit)])
mixer.colorButton2.configure(command = lambda: [generator.setColor(toolkit, mixer.hexInput2, mixer.colorOutput2), mixer.setSpectrum(toolkit), editor.displayColor(editor.currShape, toolkit)])
artist.clearButton.configure(command = lambda: [canvas.delete('all'), artist.lineMode("")])

# make colors clickable
toolkit.tag_bind(generator.colorOutput, '<Button-1>', lambda _: editor.colorClick(generator.colorOutput, toolkit))
toolkit.tag_bind(hsvgenerator.colorOutput, '<Button-1>', lambda _: editor.colorClick(hsvgenerator.colorOutput, toolkit))
toolkit.tag_bind(mixer.colorOutput1, '<Button-1>', lambda _: editor.colorClick(mixer.colorOutput1, toolkit))
toolkit.tag_bind(mixer.colorOutput2, '<Button-1>', lambda _: editor.colorClick(mixer.colorOutput2, toolkit))
toolkit.tag_bind(mixer.spectrum[0], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[0], toolkit))
toolkit.tag_bind(mixer.spectrum[1], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[1], toolkit))
toolkit.tag_bind(mixer.spectrum[2], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[2], toolkit))
toolkit.tag_bind(mixer.spectrum[3], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[3], toolkit))
toolkit.tag_bind(mixer.spectrum[4], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[4], toolkit))
toolkit.tag_bind(mixer.spectrum[5], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[5], toolkit))
toolkit.tag_bind(mixer.spectrum[6], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[6], toolkit))
toolkit.tag_bind(mixer.spectrum[7], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[7], toolkit))
toolkit.tag_bind(mixer.spectrum[8], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[8], toolkit))
toolkit.tag_bind(mixer.spectrum[9], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[9], toolkit))
toolkit.tag_bind(mixer.spectrum[10], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[10], toolkit))
toolkit.tag_bind(mixer.spectrum[11], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[11], toolkit))
toolkit.tag_bind(mixer.spectrum[12], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[12], toolkit))
toolkit.tag_bind(mixer.spectrum[13], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[13], toolkit))
toolkit.tag_bind(mixer.spectrum[14], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[14], toolkit))
toolkit.tag_bind(mixer.spectrum[15], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[15], toolkit))
toolkit.tag_bind(mixer.spectrum[16], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[16], toolkit))
toolkit.tag_bind(mixer.spectrum[17], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[17], toolkit))
toolkit.tag_bind(mixer.spectrum[18], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[18], toolkit))
toolkit.tag_bind(mixer.spectrum[19], '<Button-1>', lambda _: editor.colorClick(mixer.spectrum[19], toolkit))
toolkit.tag_bind(editor.palette[0], '<Button-1>', lambda _: editor.paletteChange(editor.palette[0], toolkit))
toolkit.tag_bind(editor.palette[1], '<Button-1>', lambda _: editor.paletteChange(editor.palette[1], toolkit))
toolkit.tag_bind(editor.palette[2], '<Button-1>', lambda _: editor.paletteChange(editor.palette[2], toolkit))
toolkit.tag_bind(editor.palette[3], '<Button-1>', lambda _: editor.paletteChange(editor.palette[3], toolkit))
toolkit.tag_bind(editor.palette[4], '<Button-1>', lambda _: editor.paletteChange(editor.palette[4], toolkit))
toolkit.tag_bind(editor.palette[5], '<Button-1>', lambda _: editor.paletteChange(editor.palette[5], toolkit))
toolkit.tag_bind(editor.palette[6], '<Button-1>', lambda _: editor.paletteChange(editor.palette[6], toolkit))
toolkit.tag_bind(editor.palette[7], '<Button-1>', lambda _: editor.paletteChange(editor.palette[7], toolkit))
toolkit.tag_bind(editor.palette[8], '<Button-1>', lambda _: editor.paletteChange(editor.palette[8], toolkit))

root.mainloop()