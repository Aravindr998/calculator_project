from tkinter import *

button = [None] * 10
window = Tk()
window.geometry("500x500")
window.title("Calculator")


def display_one():
    label.config(text=1)


def display_two():
    label.config(text=2)


def display_three():
    label.config(text=3)


def display_four():
    label.config(text=4)


def display_five():
    label.config(text=5)


def display_six():
    label.config(text=6)


def display_six():
    label.config(text=6)


def display_seven():
    label.config(text=7)


def display_eight():
    label.config(text=8)


def display_nine():
    label.config(text=9)


def display_zero():
    label.config(text=0)


def display_plus():
    label.config(text='+')


def display_minus():
    label.config(text='-')


def display_mult():
    label.config(text='*')


def display_div():
    label.config(text='/')


def display_equal():
    label.config(text='=')


def clear():
    label.config(text="")


def display_point():
    label.config(text='.')


button_one = Button(window, text=1, width=4, height=2, command=display_one)
button_two = Button(window, text=2, width=4, height=2, command=display_two)
button_three = Button(window, text=3, width=4, height=2, command=display_three)
button_four = Button(window, text=4, width=4, height=2, command=display_four)
button_five = Button(window, text=5, width=4, height=2, command=display_five)
button_six = Button(window, text=6, width=4, height=2, command=display_six)
button_seven = Button(window, text=7, width=4, height=2, command=display_seven)
button_eight = Button(window, text=8, width=4, height=2, command=display_eight)
button_nine = Button(window, text=9, width=4, height=2, command=display_nine)
button_zero = Button(window, text=0, width=4, height=2, command=display_zero)
clear_button = Button(window, text="C", width=4, height=2, command=clear)
plus_button = Button(window, text="+", width=4, height=5, command=display_plus)
minus_button = Button(window, text="-", width=4, height=2, command=display_minus)
mult_button = Button(window, text="*", width=4, height=2, command=display_mult)
div_button = Button(window, text="/", width=4, height=2, command=display_div)
equal_button = Button(window, text='=', width=4, height=5, command=display_equal)
point_button = Button(window, text='.', width=4, height=2, command=display_point)
del_button = Button(window, text='Del', width=4, height=2, command=clear)


button_zero.grid(row=6, column=2)
button_one.grid(row=5, column=1)
button_two.grid(row=5, column=2)
button_three.grid(row=5, column=3)
button_four.grid(row=4, column=1)
button_five.grid(row=4, column=2)
button_six.grid(row=4, column=3)
button_seven.grid(row=3, column=1)
button_eight.grid(row=3, column=2)
button_nine.grid(row=3, column=3)
clear_button.grid(row=2, column=1)
div_button.grid(row=2, column=2)
mult_button.grid(row=2, column=3)
minus_button.grid(row=2, column=4)
plus_button.grid(rowspan=2, row=3, column=4)
equal_button.grid(rowspan=2, row=5, column=4)
point_button.grid(row=6, column=3)
del_button.grid(row=6, column=1)

label = Label(window, text="", bg="gray", width=21, height=2, anchor=E)
label.grid(row=1, columnspan=4, column=1)
window.mainloop()

