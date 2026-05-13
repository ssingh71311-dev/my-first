import turtle
import random
 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
MOVE_DISTANCE = 20
 
DIRECTIONS = {
    "up":    (0, MOVE_DISTANCE),
    "down":  (0, -MOVE_DISTANCE),
    "left":  (-MOVE_DISTANCE, 0),
    "right": (MOVE_DISTANCE, 0)
}
 
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
current_direction = "up"
 
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("darkgreen")
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.tracer(0)
 
pen = turtle.Turtle("square")
pen.color("lightgreen")
pen.penup()
 
food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.penup()
food.shapesize(stretch_wid=0.5, stretch_len=0.5)
 
def reposition_food():
    x = random.randint(-SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH // 2 - 20)
    y = random.randint(-SCREEN_HEIGHT // 2 + 20, SCREEN_HEIGHT // 2 - 20)
    food.goto(x, y)
 
reposition_food()
 
def draw_snake():
    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()
 
def change_direction(new_dir):
    global current_direction
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if new_dir != opposites.get(current_direction):
        current_direction = new_dir
 
window.listen()
window.onkeypress(lambda: change_direction("up"), "Up")
window.onkeypress(lambda: change_direction("down"), "Down")
window.onkeypress(lambda: change_direction("left"), "Left")
window.onkeypress(lambda: change_direction("right"), "Right")
 
while True:
    window.update()
    head_x, head_y = snake[-1]
    dx, dy = DIRECTIONS[current_direction]
    new_head = [head_x + dx, head_y + dy]
 
    if new_head in snake[:-1]:
        snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
        current_direction = "up"
        reposition_food()
        draw_snake()
        continue
 
    snake.append(new_head)
 
    if (abs(new_head[0] - food.xcor()) < 20 and
            abs(new_head[1] - food.ycor()) < 20):
        reposition_food()
    else:
        snake.pop(0)
 
    draw_snake()
 
window.mainloop()