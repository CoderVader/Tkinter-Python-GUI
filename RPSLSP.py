import random
import tkinter as tk

# Initialize TKinter window
window = tk.Tk()

# Window dimensions
window.geometry("450x450")
window.title("Rock Paper Scissors Lizard Spock")

# Intialising the Scores
user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

def choice_to_number(choice):
    rps = {'rock' : 0, 'paper' : 1, 'scissor' : 2, 'lizard': 3, 'spock' : 4}
    return rps[choice]


def number_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissor', 3: 'lizard', 4: 'spock'}
    return rps[number]

# Randomizing computer's choice
def random_compChoice():
    return random.choice(['rock', 'paper', 'scissor', 'lizard', 'spock'])


# Score calculation function
def result(human_choice, comp_choice):
    global user_score
    global comp_score

    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)

    if(user == comp):
        print('Its a Tie! Go again.')

    elif((user-comp)%5 == 1):
        print('You win! Yaay!')
        user_score += 1

    else:
        print('Oops! You lose!')
        comp_score += 1

    text_area = tk.Text(master=window, height=15, width=35, bg="#FFFF99")
    text_area.grid(column = 0, row = 6)

    answer = "Your choice: {uc}  \nComputer's Choice : {cc} \n Your Score : {u} \n Computer's Score : {c}".format(uc=user_choice, cc=comp_choice, u=user_score, c=comp_score)
    text_area.insert(tk.END, answer)

# Functions for each move.
def rock():

    global user_choice
    global comp_choice
    user_choice='rock'
    comp_choice=random_compChoice()
    result(user_choice, comp_choice)

def paper():

    global user_choice
    global comp_choice
    user_choice = 'paper'
    comp_choice = random_compChoice()
    result(user_choice, comp_choice)

def scissor():

    global user_choice
    global comp_choice
    user_choice = 'scissor'
    comp_choice = random_compChoice()
    result(user_choice, comp_choice)

def lizard():

    global user_choice
    global comp_choice
    user_choice = 'lizard'
    comp_choice = random_compChoice()
    result(user_choice, comp_choice)

def spock():

    global user_choice
    global comp_choice
    user_choice = 'spock'
    comp_choice = random_compChoice()
    result(user_choice, comp_choice)

# Button Settings
button1 = tk.Button(text="    Rock    ",bg="#FFFF88", command=rock)
button1.grid(column=0,row=1)

button2 = tk.Button(text="    Paper    ",bg="#FFFF34", command=paper)
button2.grid(column=0,row=2)

button3 = tk.Button(text="    Scissor    ",bg="#FFFF77", command=scissor)
button3.grid(column=0,row=3)

button4 = tk.Button(text="    Lizard    ",bg="#FFFF77", command=lizard)
button4.grid(column=0,row=4)

button5 = tk.Button(text="    Spock    ",bg="#FFFF77", command=spock)
button5.grid(column=0,row=5)

window.mainloop()
