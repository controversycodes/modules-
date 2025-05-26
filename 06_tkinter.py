import tkinter as tk
#created a window
root = tk.Tk()
#crating width abd size 
root.geometry("1200x900")
root.maxsize(1200,1000)
root.minsize(500,300)
#creating lables
lable = tk.Label(text="Calculater")

lable.pack()
button = tk.Button(text='quikt', bg= 'green')
button.pack()

root.mainloop()