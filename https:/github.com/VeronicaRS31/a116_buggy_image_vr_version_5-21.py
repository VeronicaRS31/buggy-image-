#   a116_buggy_image.py
import turtle as trtl
# this first 3 lines of code does the body of the spider
spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(20)

num_legs = 6 
#this variable determines the number of legs your spider has
leg_lenght = 70
# this variable determines the lenght of the legs of spider
distance_legs = 380 / num_legs
# this variable determines how far apart the legs of the spdider are from each other
print("distance_legs=", distance_legs)
spider_body.pensize(5)
n = 0
#this while loop adds a leg and repositions the new leg based on the distance of your legs.
#  The end result of this loop is the body of the spider with the # of legs you decided on
while (n < num_legs):
  spider_body.goto(0,0)
  spider_body.setheading(distance_legs*n)
  print("distance_legs*n=", distance_legs*n)
  spider_body.forward(leg_lenght)
  n = n + 1
spider_body.hideturtle()

wn = trtl.Screen()
