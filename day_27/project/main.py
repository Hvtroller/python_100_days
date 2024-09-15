from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
eqlabel = Label(text="is equal to")
eqlabel.grid(column=0, row=1)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# Label
label = Label(text="0")
label.grid(column=1, row=1)

# Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
def button_clicked():
    miles = float(entry.get())
    km = miles * 1.60934
    label["text"] = km

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
