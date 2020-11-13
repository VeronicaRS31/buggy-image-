#   a116_buggy_image.py
import turtle as trtl

spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(20)

num_legs = 6 
leg_lenght = 70
distance_legs = 380 / num_legs
print("distance_legs=", distance_legs)
spider_body.pensize(5)
n = 0

while (n < num_legs):
  spider_body.goto(0,0)
  spider_body.setheading(distance_legs*n)
  print("distance_legs*n=", distance_legs*n)
  spider_body.forward(leg_lenght)
  n = n + 1
  
spider_body.hideturtle()
wn = trtl.Screen()
