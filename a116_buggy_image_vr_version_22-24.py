#   a116_buggy_image.py
#this program draws a spider
import turtle as trtl

# these first 3 lines draw the body of the spider
spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(20)
 
# these lines just give spider leg information, pensize, and other characteristics
num_legs = 6 # the number of legs of your spider
leg_lenght = 70 # the length of your legs, bassically how long they are
distance_legs = 380 / num_legs # the degree of each leg, this separates the legs each time the loop is done
spider_body.pensize(5)
n = 0

# this draws the # of legs you defined previously
while (n < num_legs):
  spider_body.goto(0,0)
  spider_body.setheading(distance_legs*n)
  spider_body.forward(leg_lenght)
  n = n + 1

# dont mess with this, as it shows you the result of your program
spider_body.hideturtle()
wn = trtl.Screen()

