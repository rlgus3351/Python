from tkinter import * 

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


#Label
my_label = Label(text = "I Am a Label", font = ("Arial", "24", "bold"))
my_label.config(text="new_text")
my_label.grid(column=0, row = 0)

#-------------------------------------------------------------------------------------------
# configuration, change


#button
def button_clicked():
    # print("I got clicked")
    new_text = input.get()


button = Button(text = "Click me", command = button_clicked)
button.grid(column=1, row = 1)


new_button = Button(text = "Click here")
new_button.grid(column=2, row = 0)

#Entry

entry = Entry(width=30)
entry.insert(END, string = "Some text to begin with.")
print(entry.get())
entry.grid(column=3, row = 2)


window.mainloop()