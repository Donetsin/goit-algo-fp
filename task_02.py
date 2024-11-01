import turtle


def draw_tree(branch_length, angle, depth):
    if depth == 0:
        return

    turtle.forward(branch_length)
    turtle.left(angle)
    draw_tree(branch_length * 0.85, angle, depth - 1)

    turtle.right(angle)
    turtle.right(angle)
    draw_tree(branch_length * 0.85, angle, depth - 1)

    turtle.left(angle)

    turtle.backward(branch_length)


screen = turtle.Screen()
screen.title("Дерево Піфагора")
turtle.speed(0)
turtle.shape("circle")
turtle.pencolor("green")
screen.bgcolor("black")

turtle.left(90)
turtle.up()
turtle.backward(200)
turtle.down()

depth = int(input("Введіть рівень рекурсії (наприклад, 10): "))
draw_tree(100, 30, depth)
screen.exitonclick()

