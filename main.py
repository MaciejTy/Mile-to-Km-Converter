from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.maxsize(width=300, height=300)
window.config(padx=20, pady=20)

kilometers = Label(window, text="0", font=("Arial", 12))
kilometers.grid(column=1, row=4)
def clicked():
    ml = float(input.get())
    km = ml*1.6
    round_km = round(km, 2)
    kilometers.config(text=str(round_km))


miles = Label(window, text="Miles", font=("Arial", 12))
miles.grid(column=2, row=3)

input = Entry(width=7)
input.grid(column=1, row=3)

is_equal_to = Label(window, text="is equal to", font=("Arial", 12))
is_equal_to.grid(column=0, row=4)

button = Button(window, text="Calculate", command=clicked)
button.grid(column=1, row=5)

kilometers_str = Label(window, text="kilometers", font=("Arial", 12))
kilometers_str.grid(column=2, row=4)










window.mainloop()