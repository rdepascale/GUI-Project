import Tkinter

root = Tkinter.Tk() # create main window
root.wm_title('CSP GUI Demo')

# Text window for information
editor = Tkinter.Text(root, width=10, height=2)
editor.grid(row=1, column=3, rowspan=1)

# Canvas creation & placement
canvas = Tkinter.Canvas(root, height = 300, width = 300, background='#FFFFFF')
canvas.grid(row=3, column=4, rowspan=1)

# Inform user of interface
######
message = Tkinter.Label(root, text='Drag sliders to\nchange color.')
message.grid(column=0, row=0, sticky=Tkinter.N)

# Instantiate 3 IntVars & create variables
red_intvar = Tkinter.IntVar()
grn_intvar = Tkinter.IntVar()
blu_intvar = Tkinter.IntVar()

# Definte a new class, an abstraction of the sliders
class ColorSlider(Tkinter.Scale):
    def __init__(self, parent, myLabel, model_intvar, editor, canvas):
        def slider_changed(new_val):
            tk_color_string = color(red_intvar, grn_intvar, blu_intvar)
            editor.delete(1.0, Tkinter.END)                 # only one hex code will show
            editor.insert(Tkinter.END, 'Hex Code\n'+tk_color_string)
            editor.see(Tkinter.END)
            canvas.itemconfig(shapes[-1],fill=tk_color_string)
        Tkinter.Scale.__init__(self, parent, orient=Tkinter.HORIZONTAL, from_=0, to=255, variable=model_intvar, label=myLabel, command=slider_changed)
        
# Create and place the sliders
red_slider = ColorSlider(root, 'Red:', red_intvar, editor, canvas)
red_slider.grid(row=1, column=0, sticky=Tkinter.W)

grn_slider = ColorSlider(root, 'Green:', grn_intvar, editor, canvas)
grn_slider.grid(row=1, column=1, sticky=Tkinter.W)

blu_slider = ColorSlider(root, 'Blue:', blu_intvar, editor, canvas)
blu_slider.grid(row=1, column=2, sticky=Tkinter.W)  

# Functions to transform Intvars into Tkinter color strings
def hexstring(slider_intvar):
    # Get an integer from an IntVar
    slider_int = slider_intvar.get()
    # Convert to hex
    slider_hex = hex(slider_int)
    # Drop the 0x at the beginning of the hex string
    slider_hex_digits = slider_hex[2:] 
    # Ensure two digits of hexadecimal:
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
    return slider_hex_digits

def color(r,g,b):
    rx=hexstring(r)
    gx=hexstring(g)
    bx=hexstring(b)
    return '#'+rx+gx+bx

# Draw a rectangle on the canvas
new_rectangle = canvas.create_rectangle(0, 50, 100, 100,  outline='#000000')
shapes=[]
shapes.append(new_rectangle)
canvas.itemconfig(shapes[0], outline='black')

# Enter event loop
root.mainloop()