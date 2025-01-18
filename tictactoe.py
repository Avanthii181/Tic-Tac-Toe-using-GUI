import tkinter as tk
from tkinter import messagebox

# Function to check the winner
def check_winner():
    for i in range(3):
        # Check rows and columns
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text']

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']

    # No winner
    return None

# Function to handle button click
def button_click(row, col):
    global current_player, winner  # Declare winner as global

    if buttons[row][col]['text'] == "" and winner is None:
        buttons[row][col].config(text=current_player)
        winner = check_winner()
        
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Function to reset the game
def reset_game():
    global current_player, winner
    current_player = 'X'
    winner = None
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")
            
# Set up the main game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize global variables
buttons = [[None, None, None] for _ in range(3)]
current_player = 'X'
winner = None

# Create buttons for the Tic-Tac-Toe grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3, font=("Arial", 20),
                                  command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Add a reset button
reset_button = tk.Button(root, text="Reset", width=10, height=2, font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Start the Tkinter main loop
root.mainloop()
