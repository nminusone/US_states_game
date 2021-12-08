from turtle import Turtle


class Draw(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.ht()
        self.penup()
        self.goto(0, 0)
        self.x = 0
        self.y = 0
        self.name = ''

    # TODO draw state name on map at correct x,y
    def write_state(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.goto(self.x, self.y)
        self.write(self.name, move=False, align='center', font=('courier', 6, 'normal'))

