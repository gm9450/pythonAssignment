# 계산기 만들기
from tkinter import *

window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg="yellow", fg="black", borderwidth=5)
display.grid(row=0, column=0, columnspan=5)
display2 = Entry(window, width=33, bg="white", fg="black", borderwidth=5)
display2.grid(row=5, column=0, columnspan=5)
display2.insert(END, '미리보기 : ')
def click(key):
    if key == '=':
        result = eval(display.get())
        display.insert(END, '=' + str(result))
        display2.delete(0, END)
        display2.insert(END, '미리보기 : ')
    elif key == 'C':
        display.delete(0, END)
        display2.delete(0, END)
        display2.insert(END, '미리보기 : ')
    else:
        display.insert(END, key)
        if not (key == ' ' or key == '+' or key == '-' or key == '*' or key == '/' or key == '%' or key == '//'):
            result = eval(display.get())
            display2.delete(0, END)
            display2.insert(END, '미리보기 : ' + str(result))

Button_list = ['7', '8', '9', '/', 'C',
               '4', '5', '6', '*', '%',
               '1', '2', '3', '-', '//',
               '0', '.', ' ', '+', '=',]

row_index = 1
col_index = 0
for button_text in Button_list:
    def process(t=button_text):
        click(t)
    if (button_text == 'C'):
        Button(window, text=button_text, width=5, bg="red",command=process).grid(row=row_index, column=col_index)
    elif (button_text == '='):
        Button(window, text=button_text, width=5, bg="green",command=process).grid(row=row_index, column=col_index)
    else:
        Button(window, text=button_text, width=5, command=process).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
