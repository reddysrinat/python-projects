import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 18", relief=tk.GROOVE, bd=5)
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", click)

root.mainloop()
