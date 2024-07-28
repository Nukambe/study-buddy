import tkinter as tk
from screeninfo import get_monitors

monitors = get_monitors()
for monitor in monitors:
    print(monitor)

root = tk.Tk()
root.title("Test Window")
root.geometry("1000x500+100+100")
root.mainloop()
