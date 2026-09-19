import tkinter as tk
from tkinter import messagebox

#setting up initial window specifications
window = tk.Tk()
window.geometry("600x400")
window.title("Practice GUI")

#labeling
label1 = tk.Label(
    window, text="This is my practice GUI", font=("Times New Roman", 16)
)
label1.pack(pady=13)
label2 = tk.Label(
    window, text="Arbitrary second label", font=("Times New Roman", 8)
)
label2.pack(padx = 10, pady=3)

#textbox practice
textbox = tk.Text(window, height=6,font=("Arial",12))
textbox.pack(padx=13)

entry1 = tk.Entry(window, font=("Arial", 12))
entry1.pack(pady=10)

#function giving functionality to special button
def outputMessage():
    if state.get()==1:
        print("special button got clicked")
    else:
        print("cant do that, have to check box first")

#checkbox practice
state = tk.IntVar()
checkbox = tk.Checkbutton(window, text="Do something?", font=("Arial", 12), variable=state)
checkbox.pack(pady=10)

#buttons
button1 = tk.Button(window, text="Special Button", font=("Arial", 14), command = outputMessage)
button1.pack(pady=10)

#radio buttons
radio = tk.StringVar()
radio1 = tk.Radiobutton(window, text="meaningless option 1", variable=radio, value="1", font=("Arial", 12))
radio1.pack(pady=5)
radio2 = tk.Radiobutton(window, text="meaningless option 2", variable=radio, value="2", font=("Arial", 12))
radio2.pack(pady=5)
radio3 = tk.Radiobutton(window, text="meaningless option 3", variable=radio, value="3", font=("Arial", 12))
radio3.pack(pady=5)

window.mainloop()


