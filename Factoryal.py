#снежинка коха
import turtle

WIDTH, HEIGHT = 1200, 700
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.delay(0)

snowH = turtle.Turtle()
snowH.pensize(5)
snowH.setpos(-WIDTH // 6, HEIGHT // 6)
snowH.color('red')
gens = 5 #больше не стоит, так как не хватает разшерения(чем больше поколений, тем более детальна у меня
axiom = 'F++F++F'
chr_1, rule_1 = 'F', 'F-F++F-F'
step = 500
angle = 60


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom]) # <-----


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


for gen in range(gens):
   
    turtle.goto(-WIDTH // 50, HEIGHT // 100)
    turtle.clear()
    snowH.setheading(0)
    snowH.goto(-WIDTH // 6, HEIGHT // 6)
    snowH.clear()

    length = step / pow(3, gen)
    for chr in axiom:
        if chr == chr_1:
            snowH.forward(length)
        elif chr == '+':
            snowH.right(angle)
        elif chr == '-':
            snowH.left(angle)

    axiom = apply_rules(axiom)

screen.exitonclick()
