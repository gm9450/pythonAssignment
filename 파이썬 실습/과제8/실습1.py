from tkinter import *
from tkinter import colorchooser

mycolor = "black"
n = 1
k = True
def paint(event):
    global n
    if (k == True):
        x1, y1 = (event.x - n), (event.y - n)
        x2, y2 = (event.x + n), (event.y + n)
        canvas.create_oval(x1, y1, x2, y2, fill=mycolor, outline=mycolor)
    elif (k == False): # 삼각형 모양
        x1, y1 = (event.x - n), (event.y - n)
        x2, y2 = (event.x + n), (event.y + n)
        x3, y3 = (event.x), (event.y - 2 * n)
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=mycolor, outline=mycolor)

def choose_color():
    global mycolor
    color = colorchooser.askcolor(title="Choose color")[0]
    mycolor = "#%02x%02x%02x" % tuple(map(int, color))
    global button_color
    button_color.destroy()
    button_color = Button(window, text=f"색상변경\n현재 색상 : {mycolor}",bg="pink",fg=mycolor,height=5, command=choose_color)
    button_color.grid(row=0, column=0)

def pen_size(k):
    global n
    if (k == 1):
        n += 0.5
    elif (k==2):
        n -= 0.5

def pen_shape():
    global k
    k = not k

window = Tk()
canvas = Canvas(window, bg="white")
canvas.grid(row=0, column=1, rowspan=2, columnspan=2)
canvas.bind("<B1-Motion>", paint)
button_color = Button(window, text=f"색상변경\n현재 색상 : {mycolor}",bg="pink",fg=mycolor,height=5, command=choose_color)
button_color.grid(row=0, column=0)
button_shape = Button(window, text="모양변경",bg="pink",fg="black",height=5, command=pen_shape)
button_shape.grid(row=1, column=0)
button_sizeup = Button(window, text="크기 증가",bg="white",fg="black", width=10,command=lambda: pen_size(1))
button_sizeup.grid(row=2, column=1)
button_sizedown = Button(window, text="크기 감소",bg="white",fg="black", width=10,command=lambda: pen_size(2))
button_sizedown.grid(row=2, column=2)
window.mainloop()