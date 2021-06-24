import turtle
import pandas

FONT = ("Ariel", 8, "normal")

#Screen setup
screen = turtle.Screen()
screen.title("US States Memory Game")
image = "blank_states_img.gif"
#screen.addshape(image)
#turtle.shape(image)
screen.bgpic(image)

#import data
data = pandas.read_csv("50_states.csv")

#get coordinates from user_answer
def get_coords(answer):
    answer_data = data[data.state == answer]
    x = int(answer_data.x)
    y = int(answer_data.y)
    return(x,y)

#plot a correct answer on the map
def plot_answer(answer,coord):
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(coord)
    turtle.write(f"{answer}", align="center", font=FONT)

all_states = data.state.to_list()
guesses = []
score = 0
game_on = True

while game_on == True:
    #get user input and convert to title case
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()
    
    #check for EXIT state
    if answer_state == "Exit":
        break
    
    #check if the answer_state is in data.state. 
    if answer_state in all_states:
        #if it hasn't already been guessed, plot it on the map after first getting the coordinates, save the guess in the guesses list, increase score
        if answer_state not in guesses:
            guesses.append(answer_state)
            score += 1
            answer_coord = get_coords(answer_state)
            plot_answer(answer_state, answer_coord)
            #if all states has been guessed, the game ends
            if score == 50:
                game_on = False


#states to learn csv
states_to_learn_list = []
for state in all_states:
    if state not in guesses:
        states_to_learn_list.append(state)

df = pandas.DataFrame(states_to_learn_list)
df.to_csv("states_to_learn.csv")
