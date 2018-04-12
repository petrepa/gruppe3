import tkinter

t = Tk() # new window
t.update()
t.attributes("-alpha", 00)
t.state('zoomed') # maximize the window
height= t.winfo_height() # ...
width= t.winfo_width()