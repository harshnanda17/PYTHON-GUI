import turtle
import time

screen = turtle.Screen() #turtle screen
screen.bgcolor("black") #background of the screen
screen.setup(width=600, height=600) #geometry of the GUI
screen.title("Analog Clock") #title of the GUI
screen.tracer(0) #tracer for the GUI

Harsh = turtle.Turtle() #the turtle
Harsh.hideturtle() #make the turtle invisible
Harsh.speed(0) #setting the speed to 0
Harsh.pensize(6) #setting the pensize to 3


def make_clock(Hours, minute, second, Harsh): #function with 4 parameters

    Harsh.up() #not ready to draw
    Harsh.goto(0, 210) #positioning the turtle
    Harsh.setheading(180) #setting the heading to 180
    Harsh.color("green") #setting the color of the pen to red
    Harsh.pendown() #starting to draw
    Harsh.circle(210) #a circle with the radius 210

    Harsh.up() #not ready to draw
    Harsh.goto(0, 0) #positioning the turtle
    Harsh.setheading(90) #same as seth(90) in newer version

    for z in range(12): #loop 
        Harsh.fd(190) #moving forward at 190 units
        Harsh.pendown() #starting to draw
        Harsh.fd(20) #forward at 20
        Harsh.penup() #not ready to draw
        Harsh.goto(0, 0) #positioning the turtle
        Harsh.rt(30) #right at an angle of 30 degrees

    hands = [("red", 80, 12), ("red", 150, 60), ("red", 110, 60)] #the color and the hands set
    time_set = (Hours, minute, second) #setting the time

    for hand in hands: #loop
        time_part = time_set[hands.index(hand)] #time part in the hand index in hands of time_Set
        angle = (time_part/hand[2])*360 #setting the angle for the clock
        Harsh.penup() #not ready to draw
        Harsh.goto(0, 0) #positioning the turtle
        Harsh.color(hand[0]) #setting the color of the hand
        Harsh.setheading(90) #same as seth(90)
        Harsh.rt(angle) #right at an angle of "right"
        Harsh.pendown() #ready to draw
        Harsh.fd(hand[1]) #forward at a unit of 1st index of the hand var


while True:
    Hours  = int(time.strftime("%I")) #setting the hour from the time module
    minute = int(time.strftime("%M")) #setting the minute from the time module
    second = int(time.strftime("%S")) #setting the second as above

    make_clock (Hours, minute, second, Harsh) #calling the ghanta_bana() function with the given parameters
    screen.update() #updating the scren
    time.sleep(1) #making the code sleep for a second with the time module
    Harsh.clear() #clearing the pen

    
