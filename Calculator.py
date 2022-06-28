from tkinter import *

button = [None] * 10
window = Tk()
window.geometry("500x500")
i: int
for i in range(10):
    button[i] = Button(window, text=i, width=4, height=2)
clear_button = Button(window, text="C", width=4, height=2)
plus_button = Button(window, text="+", width=4, height=5)
minus_button = Button(window, text="-", width=4, height=2)
mult_button = Button(window, text="*", width=4, height=2)
div_button = Button(window, text="/", width=4, height=2)
equal_button = Button(window, text='=', width=4, height=5)
point_button = Button(window, text='.', width=4, height=2)
del_button = Button(window, text='Del', width=4, height=2)

button[0].grid(row=6, column=2)
button[1].grid(row=5, column=1)
button[2].grid(row=5, column=2)
button[3].grid(row=5, column=3)
button[4].grid(row=4, column=1)
button[5].grid(row=4, column=2)
button[6].grid(row=4, column=3)
button[7].grid(row=3, column=1)
button[8].grid(row=3, column=2)
button[9].grid(row=3, column=3)
clear_button.grid(row=2, column=1)
div_button.grid(row=2, column=2)
mult_button.grid(row=2, column=3)
minus_button.grid(row=2, column=4)
plus_button.grid(rowspan=2, row=3, column=4)
equal_button.grid(rowspan=2, row=5, column=4)
point_button.grid(row=6, column=3)
del_button.grid(row=6, column=1)

window.mainloop()
print('ok')
