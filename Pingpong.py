import turtle
import time

pencere = turtle.Screen()
pencere.title("PinPong")
pencere.bgcolor("black")
pencere.setup(width=800,height=600)
pencere.tracer(0)

raket_sol = turtle.Turtle()
raket_sol.speed(0)
raket_sol.shape('square')
raket_sol.color('white')
raket_sol.penup()
raket_sol.goto(-350,0)
raket_sol.shapesize(5, 1)

raket_sag = turtle.Turtle()
raket_sag.speed(0)
raket_sag.shape('square')
raket_sag.color('white')
raket_sag.penup()
raket_sag.goto(350,0)
raket_sag.shapesize(5, 1)

top = turtle.Turtle()
top.speed(0)
top.shape('circle')
top.color('white')
top.penup()
top.dx = 0.1
top.dy = 0.1

yazi = turtle.Turtle()
yazi.speed(0)
yazi.color('white')
yazi.penup()
yazi.goto(0,260)
yazi.write("Oyuncu Sol:0   Oyuncu Sağ:0",align='center',font=('Courier',24,'bold'))
yazi.hideturtle()
puan_sol = 0
puan_sag = 0


def raket_sol_up():
    y = raket_sol.ycor()
    y = y + 20
    raket_sol.sety(y)

def raket_sol_down():
    y = raket_sol.ycor()
    y = y - 20
    raket_sol.sety(y)

def raket_sag_up():
    y = raket_sag.ycor()
    y = y + 20
    raket_sag.sety(y)

def raket_sag_down():
    y = raket_sag.ycor()
    y = y - 20
    raket_sag.sety(y)


pencere.listen()
pencere.onkeypress(raket_sol_up,'w')
pencere.onkeypress(raket_sol_down,'s')
pencere.onkeypress(raket_sag_up,'Up')
pencere.onkeypress(raket_sag_down,'Down')

while True:
    pencere.update()
    top.setx(top.xcor() + top.dx)
    top.sety(top.ycor() + top.dy)

    if top.ycor() > 290 or top.ycor() < -290:
        top.dy = top.dy * -1 

    if top.xcor() > 390:
        top.goto(0,0)
        top.dx = top.dx * -1
        puan_sol = puan_sol + 1
        yazi.clear()
        yazi.write("Oyuncu Sol:{}   Oyuncu Sağ:{}".format(puan_sol,puan_sag) , align='center', font=('Courier',24,'bold'))
    if top.xcor() < -390:
        top.goto(0,0)
        top.dx = top.dx * -1 
        puan_sag = puan_sag + 1
        yazi.clear()
        yazi.write("Oyuncu Sol:{}   Oyuncu Sağ:{}".format(puan_sag,puan_sol),align='center',font=('Courier',24,'bold'))

    if (top.xcor() > 340 and top.xcor() < 350) and (top.ycor() < raket_sag.ycor()+60 and top.ycor() > raket_sag.ycor() -60):
        top.setx(340)
        top.dx = top.dx * -1

    if (top.xcor() < -340 and top.xcor() > -350) and (top.ycor() < raket_sol.ycor()+60 and top.ycor() > raket_sol.ycor() -60):
        top.setx(-340)
        top.dx = top.dx * -1           

    if puan_sag == 5 or puan_sol == 5:
        if puan_sag == 5:
            yazi.clear()
            yazi.write("Tebrikler Oyuncu Sağ!",align='center',font=('Courier',24,'bold'))
        else:
            yazi.clear()
            yazi.write("Tebrikler Oyunsu Sol!",align='center',font=('Courier',24,'bold'))
        yazi.hideturtle()
        
        cevap = pencere.textinput("Tekrar Oyna","Tekrar Oynamak İçin 'E' veya 'H' giriniz.") 
        
        if cevap and cevap.lower() == 'e':
            yazi.write("Oyuncu Sol:0   Oyuncu Sağ:0",align='center',font=('Courier',24,'bold'))
            puan_sol = 0
            puan_sag = 0
            top.goto(0,0)
            top.dx = top.dx * -1
            raket_sag.goto(350,0)
            raket_sol.goto(-350,0)
            yazi.clear()
        else:
            break    

pencere.mainloop()

        
    