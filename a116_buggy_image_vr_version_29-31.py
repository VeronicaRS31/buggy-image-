#   a116_buggy_image.py
#this program draws a spider
import turtle as trtl

# these first 3 lines draw the body of the spider
spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(20)

#these lines draw the head of the spider
spider_body.goto(0,-25)
spider_body.pensize(15)
spider_body.circle(10)
 
# these lines just give spider leg information, pensize, and other characteristics
num_legs = 8 # the number of legs of your spider
leg_lenght = 70 # the length of your legs, bassically how long they are
distance_legs = 240 / num_legs # the degree of each leg, this separates the legs each time the loop is done
spider_body.pensize(5)

n = 0
# this draws the # of legs you defined previously
while (n < num_legs/2):
  spider_body.goto(0,20)
  spider_body.setheading(distance_legs*n -45)
  spider_body.forward(leg_lenght)
  n = n + 1

n=0
while (n < num_legs/2):
  spider_body.goto(0,20)
  spider_body.setheading(distance_legs*n -45 +180)
  spider_body.forward(leg_lenght)
  n = n + 1

# eyes of this creepy spider :)
spider_body.pencolor("white")
spider_body.penup()
spider_body.goto(5,-15)
spider_body.pendown()
spider_body.fillcolor("white")
spider_body.begin_fill()
spider_body.circle(5)
spider_body.end_fill()
spider_body.penup()
spider_body.goto(-15,-15)
spider_body.pendown()
spider_body.fillcolor("white")
spider_body.begin_fill()
spider_body.circle(5)
spider_body.end_fill()

# dont mess with this, as it shows you the result of your program
spider_body.hideturtle()
wn = trtl.Screen()

