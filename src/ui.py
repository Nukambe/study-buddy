import tkinter as tk

def on_button_click():
    user_input = entry.get()
    tk.messagebox.showinfo("Information", f"Hello, {user_input}!")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Study Buddy")
    root.geometry("800x500")

    default_font = ('Arial', 18)

    label = tk.Label(root, text="Hello, World!", font=default_font)
    label.pack(padx=20, pady=20)

    textbox = tk.Text(root, font=default_font, height=3, padx=10)
    textbox.pack()

    entry = tk.Entry(root)
    entry.pack()

    buttons = []
    button_frame = tk.Frame(root)
    for i in range(0, 3):
        button_frame.columnconfigure(i, weight=1)
        btn = tk.Button(button_frame, text=f'click me {i + 1}', font=default_font)
        btn.grid(row=0, column=i, sticky=tk.W+tk.E)
        buttons.append(btn)
    button_frame.pack(fill="x")


    # Start the main event loop
    root.mainloop()

# if __name__ == "__main__":
#     main()
