from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()

root.title("XO Game")
#root.iconbitmap('xo.ico')
root.configure(background='black')
x = 0
image1 = Image.open('o.png')
image1 = image1.resize((130, 75), Image.ANTIALIAS)
x_image = ImageTk.PhotoImage(image1)

image2 = Image.open('x.png')
image2 = image2.resize((130, 75), Image.ANTIALIAS)
o_image = ImageTk.PhotoImage(image2)


Label(root, text="Enter Player 1 name (X): ", bg='black', fg='white').grid(row=0, column=0)
entry1 = Entry(root)
entry1.grid(row=0, column=1)
Label(root, text="Enter Player 2 name (O): ", bg='black', fg='white').grid(row=1, column=0)
entry2 = Entry(root)
entry2.grid(row=1, column=1)
turn_label = Label(root)

def start():
    global entry1, entry2, x, turn_label
    if entry1.get() != "" and entry2 != "":
        btn1["state"] = NORMAL
        btn2["state"] = NORMAL
        btn3["state"] = NORMAL
        btn4["state"] = NORMAL
        btn5["state"] = NORMAL
        btn6["state"] = NORMAL
        btn7["state"] = NORMAL
        btn8["state"] = NORMAL
        btn9["state"] = NORMAL
        start_btn["state"] = DISABLED
        entry1.config(state="disabled")
        entry2.config(state="disabled")
        turn_label = Label(root, text=f'{entry1.get()} turn to play (X)', bg='red', fg='white')
        turn_label.grid(row=2, column=1)

    else:
        messagebox.showwarning("Error", "Please Enter players names")

start_btn = Button(root, text="START", relief=GROOVE, command=start)
start_btn.grid(row=2, column=0)

def show_winner():
    global winner
    messagebox.showinfo("Winner", f'{winner} WON!!')
    root.quit()
def check():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    if btn1["text"] == btn2["text"] == btn3["text"] != "  ": show_winner()
    elif btn4["text"] == btn5["text"] == btn6["text"] != "  ": show_winner()
    elif btn7["text"] == btn8["text"] == btn9["text"] != "  ": show_winner()
    elif btn1["text"] == btn4["text"] == btn7["text"] != "  ": show_winner()
    elif btn2["text"] == btn5["text"] == btn8["text"] != "  ": show_winner()
    elif btn3["text"] == btn6["text"] == btn9["text"] != "  ": show_winner()
    elif btn1["text"] == btn5["text"] == btn9["text"] != "  ": show_winner()
    elif btn3["text"] == btn5["text"] == btn7["text"] != "  ": show_winner()
    elif btn1["text"] != "  " and btn2["text"] != "  " and btn3["text"] != "  " and btn4["text"] != "  " and btn5["text"] != "  " and btn6["text"] != "  " and\
        btn7["text"] != "  " and btn8["text"] != "  " and btn9["text"] != "  ":
        messagebox.showinfo("Winner", "Draw !!")
        root.quit()

def player_select(button):
    global x, winner, turn_label, x_image, o_image

    button["state"] = DISABLED
    if x % 2 == 0:
        button["text"] = "o"
        button["image"] = o_image

        winner = entry1.get()
    elif x % 2 != 0:
        button["text"] = "x"
        button["image"] = x_image
        winner = entry2.get()
    check()
    x += 1
    if x % 2 == 0:
        turn_label.grid_remove()
        turn_label = Label(root, text=f'{entry1.get()} turn to play (X)')
        turn_label.configure(bg='red')
        turn_label.configure(fg='white')
        turn_label.grid(row=2, column=1)
    elif x % 2 != 0:
        turn_label.grid_remove()
        turn_label = Label(root, text=f'{entry2.get()} turn to play (O)')
        turn_label.configure(bg='blue')
        turn_label.configure(fg='white')
        turn_label.grid(row=2, column=1)



btn1 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn3))
btn3.grid(row=3, column=2)
btn4 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn4))
btn4.grid(row=4, column=0)
btn5 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn5))
btn5.grid(row=4, column=1)
btn6 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn6))
btn6.grid(row=4, column=2)
btn7 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn7))
btn7.grid(row=5, column=0)
btn8 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn8))
btn8.grid(row=5, column=1)
btn9 = Button(root, text="  ", padx=60, pady=30, relief=GROOVE, state=DISABLED, command=lambda: player_select(btn9))
btn9.grid(row=5, column=2)

root.mainloop()

