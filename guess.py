import csv
from turtle import Turtle
import pandas as pd


class Guessing:
    def __init__(self):
        self.user_guess = ''
        self.csv_list = pd.read_csv('50_states.csv')
        self.states = self.csv_list['state']
        self.csv_dict = self.csv_list.to_dict()
        self.guess_list = []
        self.row_mask = []
        self.x = 0
        self.y = 0
        self.x_from_dict = []
        self.y_from_dict = []
        self.result = 0

    def guess_to_check(self, user_input):
        # input guess from user prompt is titled
        self.user_guess = user_input.title()
        print(self.user_guess)

    def check_list(self):
        if self.user_guess in self.states.unique():
            self.guess_list.append(self.user_guess)
            self.get_xy()
            print(self.guess_list)
            return True

    def get_xy(self):
        self.row_mask = self.csv_list.loc[self.csv_list['state'] == self.user_guess]
        self.x = self.row_mask['x']
        self.y = self.row_mask['y']
        # print(self.csv_dict)
        # #self.x_from_dict=self.csv_dict[self.user_guess]
        # if 'Alabama' in self.csv_dict:
        #     print('true')
        # else:
        #     print('false')

        # self.row_mask = self.csv_list[self.csv_list[self.user_guess].isin(['state'])]
        # self.row_mask = self.csv_list.isin(self.user_guess).all(1)

# TODO get the iloc of the state
# TODO pull the x, y values
