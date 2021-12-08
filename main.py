from turtle import Turtle, Screen

import pandas as pd

from guess import Guessing
from draw import Draw

# https://app.diagrams.net/#G1bqn0MwiPbI9hHwTxzdv4ZQm7VaMR4YC8

screen = Screen()
background_map = Turtle()
answer_state = Guessing()
sam = Draw()
# title
screen.title('U.S. States Game')
# Image used as the background of game
image = 'blank_states_img.gif'
# add a shape so that image can be created
screen.addshape(image)
# instead of drawing 'turtle' or 'circle' etc., draws the image defined
background_map.shape(image)
# Window pops up and asks for state

while len(answer_state.guess_list) < 50:
    answer_state.guess_to_check(screen.textinput(title=f'{len(answer_state.guess_list)}/50 States Correct', prompt=
    "Type the name of a state!"))
    if answer_state.user_guess == 'Exit':
        break
    if answer_state.check_list():
        sam.write_state(int(answer_state.x), int(answer_state.y), answer_state.user_guess)

# This is how csv values were determined
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
if len(answer_state.guess_list) < 50:
    states_to_learn = list(set(answer_state.states) - set(answer_state.guess_list))
    to_study= pd.DataFrame(states_to_learn, columns=['States you missed'])
    to_study.to_csv('Study_this.csv')
    print(states_to_learn)
