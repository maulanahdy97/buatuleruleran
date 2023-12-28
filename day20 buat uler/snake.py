from turtle import Screen, Turtle
starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        uler1 = Turtle("square")
        uler1.color("white")
        uler1.penup()
        uler1.goto(position)
        self.segment.append(uler1)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(move_distance)


    def moveup(self): # pretty obvious what these do
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def moveleft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def moveright(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def movedown(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)