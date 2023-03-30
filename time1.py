import time

import tkinter as tk
app=tk.Tk()
app.title("L'heure")
label=tk.Label(app,text=time)
app.mainloop()
label.pack()
tim=time.strftime("%H:%I:%S")
print(tim)