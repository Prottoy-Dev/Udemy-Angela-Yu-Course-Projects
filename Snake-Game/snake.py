from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []  # List to store the snake's segments (Turtle objects)
        self.create_snake()  # Create the initial snake segments
        self.head = self.body[0]  # Reference to the snake's head segment

    def create_snake(self):
        # Create the initial segments of the snake
        x_positions = [0, -20, -40]  # Initial X positions of snake segments
        for pos in x_positions:
            self.add_segment(pos)

    def add_segment(self, pos):
        # Add a new segment to the snake at the specified position
        timmy = Turtle()
        timmy.penup()
        timmy.shape("square")
        timmy.color("white")
        timmy.goto(pos, 0)
        self.body.append(timmy)

    def reset(self):
        # Reset the snake to its initial state
        for seg in self.body:
            seg.goto(10000, 0)  # Move segments out of view
        self.body.clear()  # Clear the list of segments
        self.create_snake()  # Recreate the initial snake
        self.head = self.body[0]  # Update the head reference

    def extend(self):
        # Add a new segment to the end of the snake, extending it
        self.add_segment(self.body[-1].xcor())

    def move(self):
        # Move the snake by updating the positions of its segments
        for t in range(len(self.body) - 1, 0, -1):
            new_x = self.body[t - 1].xcor()
            new_y = self.body[t - 1].ycor()
            self.body[t].goto(new_x, new_y)
        self.head.forward(20)  # Move the head segment forward

    def up(self):
        # Change the snake's direction to up (if not currently moving down)
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        # Change the snake's direction to down (if not currently moving up)
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        # Change the snake's direction to left (if not currently moving right)
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        # Change the snake's direction to right (if not currently moving left)
        if self.head.heading() != 180:
            self.head.setheading(0)
