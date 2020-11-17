#снежинка коха
import turtle

WIDTH, HEIGHT = 1280, 960
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.delay(0)
snowH = turtle.Turtle()
snowH.pensize(2)
snowH.setpos(-WIDTH // 4, HEIGHT // 5) #эксперементировал с началом, чтоб он лежал на треугольнике и не портило картинку и не выехджало
snowH.color('red')
gens = 5 #больше не стоит, так как не хватает разшерения(чем больше поколений, тем более детальна у меня
axiom = 'F++F++F'
chr_1, rule_1 = 'F', 'F-F++F-F'  #про гены(которые запоминают предыдущее состояние) и cам алгоритм L с его аксиомами я взял из источников
step = 500
angle = 60 #можно брать и 90 и 45 и тд, главное чтоб хватало замкнуть


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom]) 


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


for gen in range(gens):
   
    turtle.goto(-WIDTH // 50, HEIGHT // 100)
    
    snowH.setheading(0)
    snowH.goto(-WIDTH // 4, HEIGHT //5)
    #snowH.clear() #если убрать #перед чисткой, то мы получим нормальную снежинку коха, а так не будет этого.
    length = step / pow(3, gen) #мы треугольник с длиной L/3 равносторонии будем распологать стороной в середене сторон предшедственика
    for chr in axiom:
        if chr == chr_1:
            snowH.forward(length)
        elif chr == '+':
            snowH.right(angle)
        elif chr == '-':
            snowH.left(angle)

    axiom = apply_rules(axiom)

screen.exitonclick()
