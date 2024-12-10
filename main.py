import turtle


screen = turtle.Screen()
screen.setup(width=800, height=600)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


def write_text(turtle, text, x, y, size, color="black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, align="center", font=("Arial", size, "bold"))


def draw_shape(turtle, shape, x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    if shape == "circle":
        turtle.circle(size)
    elif shape == "square":
        for _ in range(4):
            turtle.forward(size)
            turtle.left(90)
    elif shape == "rectangle":
        for _ in range(2):
            turtle.forward(size * 2)
            turtle.left(90)
            turtle.forward(size)
            turtle.left(90)
    elif shape == "triangle":
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    turtle.end_fill()


def intro_page():
    screen.bgcolor("purple")
    write_text(pen, "This is my all about me project!!!", 0, 200, 24)
    write_text(pen, "Press Enter to move to the next page", 0, -250, 16)
    draw_shape(pen, "circle", -100, 0, 50, "blue")


def favorite_foods():
    screen.bgcolor("orange")
    write_text(pen, "My Favorite Foods", 0, 200, 24)
    write_text(pen, "Press Enter to continue", 0, -250, 16)
    draw_shape(pen, "rectangle", -200, 50, 50, "lightgreen")  # Food 1


def hobbies_page():
    screen.bgcolor("pink")
    write_text(pen, "My Hobbies", 0, 200, 24)
    write_text(pen, "Press Enter to continue", 0, -250, 16)
    draw_shape(pen, "triangle", -150, 0, 50, "black")  # Hobby 1


def favorite_movie():
    screen.bgcolor("green")
    write_text(pen, "My Favorite Movie", 0, 200, 24)
    write_text(pen, "Press Enter to continue", 0, -250, 16)
    draw_shape(pen, "rectangle", -150, -50, 100, "yellow") # Movie


def favorite_sport():
    screen.bgcolor("aquamarine")
    write_text(pen, "My Favorite Sport", 0, 200, 24)
    write_text(pen, "Press Enter to end", 0, -250, 16)
    draw_shape(pen, "circle", -150, 0, 50, "red")   # Sport
    # Sport


pages = [intro_page, favorite_foods, hobbies_page, favorite_movie, favorite_sport]
current_page = 0


def next_page():
    global current_page
    if current_page < len(pages):
        pen.clear()
        pages[current_page]()
        current_page += 1
    else:
        turtle.bye()


screen.listen()
screen.onkey(next_page, "Return")


next_page()


turtle.done()
