from tkinter import *

root = Tk()
root.geometry("350x550")
root.title("Tic Tac Toe AI")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Tic Tac Toe AI", font=("Helvetica", 20), bg="alice blue", width=15)
titleLabel.grid(row=0, column=0)

frame2 = Frame(root)
frame2.pack()

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

turn = "x"
game_end = False


def updateBoard():
    for key in board.keys():
        buttons[key - 1]["text"] = board[key]


def Winner(player):
    if board[1] == board[2] and board[1] == board[3] and board[3] == player:
        return True

    elif board[4] == board[5] and board[4] == board[6] and board[6] == player:
        return True

    elif board[7] == board[8] and board[7] == board[9] and board[9] == player:
        return True

    elif board[1] == board[4] and board[1] == board[7] and board[7] == player:
        return True

    elif board[2] == board[5] and board[2] == board[8] and board[8] == player:
        return True

    elif board[3] == board[6] and board[3] == board[9] and board[9] == player:
        return True

    elif board[1] == board[5] and board[1] == board[9] and board[9] == player:
        return True

    elif board[3] == board[5] and board[3] == board[7] and board[7] == player:
        return True

    else:
        return False


def GameDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True


def NewGame():
    global game_end

    game_end = False
    for button in buttons:
        button["text"] = " "

    for i in board.keys():
        board[i] = " "

    titleLabel = Label(frame1, text="Tic Tac Toe AI", font=("Helvetica", 20), bg="alice blue", width=15)
    titleLabel.grid(row=0, column=0)


def playAI():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "o"
            score = minimax(board, False)
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestMove = key

    board[bestMove] = "o"


def playGame(event):
    global turn, game_end

    if game_end:
        return
    button = event.widget

    buttonText = str(button)
    checkClicked = buttonText[-1]

    if checkClicked == "n":
        checkClicked = 1
    else:
        checkClicked = int(checkClicked)

    if button["text"] == " ":
        if turn == "x":

            board[checkClicked] = turn

            if Winner(turn):
                winLabel = Label(frame1, text=f"Player {turn} won!", font=("Helvetica", 24), height=1, bg="pale goldenrod")
                winLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            turn = "o"

            playAI()
            if Winner(turn):
                if turn == "o":
                    winningPlayer = "AI"
                else:
                    winningPlayer = turn
                winLabel = Label(frame1, text=f"Player {winningPlayer} won!", font=("Helvetica", 24), height=1,
                                 bg="pale goldenrod")
                winLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            turn = "x"

            updateBoard()


        else:
            button["text"] = "◯"
            board[checkClicked] = turn

            if Winner(turn):
                winLabel = Label(frame1, text=f"Player ◯ won!", font=("Helvetica", 24), height=1, bg="pale goldenrod")
                winLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            turn = "x"

        if GameDraw():
            drawLabel = Label(frame1, text=f"Game Draw!", font=("Helvetica", 24), height=1, bg="pale goldenrod")
            drawLabel.grid(row=0, column=0, columnspan=3)

        print(board)


def minimax(board, isMaximizing):
    if Winner("o"):
        return 1

    if Winner("x"):
        return -1

    if GameDraw():
        return 0

    if isMaximizing:
        bestScore = -100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "o"
                score = minimax(board, False)  # minimax
                board[key] = " "
                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = 100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "x"
                score = minimax(board, True)  # minimax
                board[key] = " "
                if score < bestScore:
                    bestScore = score

        return bestScore


# First Row
button1 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button1.grid(row=0, column=0)
button1.bind("<Button-1>", playGame)

button2 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button2.grid(row=0, column=1)
button2.bind("<Button-1>", playGame)

button3 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button3.grid(row=0, column=2)
button3.bind("<Button-1>", playGame)

# Second Row

button4 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button4.grid(row=1, column=0)
button4.bind("<Button-1>", playGame)

button5 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button5.grid(row=1, column=1)
button5.bind("<Button-1>", playGame)

button6 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button6.grid(row=1, column=2)
button6.bind("<Button-1>", playGame)

# Third Row

button7 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button7.grid(row=2, column=0)
button7.bind("<Button-1>", playGame)

button8 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button8.grid(row=2, column=1)
button8.bind("<Button-1>", playGame)

button9 = Button(frame2, text=" ", width=4, height=2, font=("Helvetica", 32), bg="gray80", relief=RAISED, borderwidth=5)
button9.grid(row=2, column=2)
button9.bind("<Button-1>", playGame)

newGame = Button(frame2, text="New Game", width=9, height=1, font=("Helvetica", 20), bg="gray79", relief=RAISED,
                 borderwidth=5, command=NewGame)
newGame.grid(row=4, column=0, columnspan=3)

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

root.mainloop()
