from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_bit = []
        self.create_snake()
        self.head = self.snake_bit[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.snake_bit.append(new_seg)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.snake_bit[-1].position())

    def move(self):
        for bit_num in range(len(self.snake_bit) - 1, 0, -1):
            new_x = self.snake_bit[bit_num - 1].xcor()
            new_y = self.snake_bit[bit_num - 1].ycor()
            self.snake_bit[bit_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)









