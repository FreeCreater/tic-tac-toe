from tkinter import Tk, Button, PhotoImage
from tkinter.messagebox import showinfo

win = Tk()
win.geometry("300x300")
win.title("Tic-tac-toe")

empty_image = PhotoImage(file="./img/empty.png")
empty_char = "_"
cross_image = PhotoImage(file="./img/cross.png")
cross_char = "X"
circle_image = PhotoImage(file="./img/circle.png")
circle_char = "O"

buttons=[]
for y in range(3):
    for x in range(3):
        button = Button(width=100, height=100, image=empty_image)
        button.place(x=x*100,y=y*100)
        button["command"] = lambda button = button ,y=y, x=x: click(button, y, x)
        buttons.append(button)

field = []
def feel_field():
    global field
    field = []
    for y in range(3):
        field.append([])
        for x in range(3):
            field[y].append(empty_char)

feel_field()

turn = 0
def click(button: Button, y, x):
    global turn
    global field

    if(field[y][x]!=empty_char):
        return
    char:str
    if(turn%2):
        button["image"] = cross_image
        char = cross_char
    else:
        button["image"] = circle_image
        char = circle_char
    field[y][x] = char
    turn+=1

    if(check_victory(y,x, char)):
        showinfo("Great game", f"{char} wins")
        restart()
        return
    if(turn == 9):
        showinfo("See you next time", "Draw")
        restart()
    

def check_victory(y,x, char)->bool:
    if (field[y][0] == char and field[y][1] == char and field[y][2] == char) or\
        (field[0][x] == char and field[1][x] == char and field[2][x] == char):
        return True
    if(x%2==1):
        return False
    if (field[0][0] == char and field[1][1] == char and field[2][2] == char) or\
        (field[0][2] == char and field[1][1] == char and field[2][0] == char):
        return True
    return False

def restart():
    global turn
    turn = 0
    feel_field()
    for button in buttons:
        button["image"] = empty_image

win.mainloop()






