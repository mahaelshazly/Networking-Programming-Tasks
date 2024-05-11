from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Welcome to The Gaming world TIC-Tac-Toe")
window.geometry("460x600")
window.configure(bg="lightblue")


title_label = Label(window, text="Tic-tac-toe Game", font=('Helvetica', '20', 'bold'), bg="#f2f2f2")
title_label.grid(row=0, column=1, pady=10)

player1_label = Label(window, text="Player 1: X", font=('Helvetica', '12'), bg="#f2f2f2")
player1_label.grid(row=1, column=1, pady=5)

player2_label = Label(window, text="Player 2: O", font=('Helvetica', '12'), bg="#f2f2f2")
player2_label.grid(row=2, column=1, pady=5)

turn = 1  # For first person turn.


def reset():
    global turn
    for btn in buttons:
        btn["text"] = " "
    turn = 1


def button_click(btn):
    global turn
    if btn["text"] == " ":
        if turn == 1:
            btn["text"] = "X"
            turn = 2
        else:
            btn["text"] = "O"
            turn = 1
        check()


def check():  # check if a win case exists
    global turn
    win_conditions = [
        [btn1, btn2, btn3],
        [btn4, btn5, btn6],
        [btn7, btn8, btn9],
        [btn1, btn4, btn7],
        [btn2, btn5, btn8],
        [btn3, btn6, btn9],
        [btn1, btn5, btn9],
        [btn7, btn5, btn3]
    ]
    for condition in win_conditions:
        symbols = [btn["text"] for btn in condition]
        if symbols[0] == symbols[1] == symbols[2] and symbols[0] in ["X", "O"]:
            messagebox.showinfo("Congratulations", f"Game complete {symbols[0]} wins")
            reset()
            return
    if all(btn["text"] != " " for btn in buttons):
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        reset()


buttons = []

for i in range(3):
    for j in range(3):
        btn = Button(window, text=" ", bg="#ffffff", fg="#000000", width=6, height=3, font=('Helvetica', '20'))
        btn.grid(row=i + 3, column=j, padx=5, pady=5)
        btn.config(command=lambda b=btn: button_click(b))
        buttons.append(btn)

btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9 = buttons

reset_btn = Button(window, text="Reset", bg="#c62c83", fg="#ffffff", width=10, font=('Helvetica', '12', 'bold'), command=reset)
reset_btn.grid(row=6, column=1, pady=10)

window.mainloop()
