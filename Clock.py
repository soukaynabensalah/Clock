import tkinter as tk

from time import strftime

def updateTime():
    time = strftime('%H:%M:%S %p')
    lbl.config(text=time)
    lbl.after(1000, updateTime)

window = tk.Tk()
window.title("clock")

lbl = tk.Label(window, font=('LCD Solid', 50, 'bold'), background='black', foreground='red',anchor="n")

lbl.pack()

updateTime()
window.mainloop()
