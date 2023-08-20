import tkinter as tk

window = tk.Tk()
text_widget = tk.Text(window)
text_widget.pack()

def insert_colored_text(text, color):
    text_widget.insert(tk.END, text, color)
    text_widget.insert(tk.END, '\n')

text_widget.tag_configure("red", foreground="red")
text_widget.tag_configure("blue", foreground="blue")
text_widget.tag_configure("green", foreground="green")

insert_colored_text("This is red text.", "red")
insert_colored_text("This is blue text.", "blue")
insert_colored_text("This is green text.", "green")

window.mainloop()
