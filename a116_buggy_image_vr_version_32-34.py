#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()


num_legs = 6
leg_lenght = 55
distance_legs = 240/ num_legs 
ladybug.pensize(5)


n = 0
# this draws the # of legs of ladybug
while (n < num_legs/2):
  ladybug.goto(0,-30)
  ladybug.setheading(distance_legs*n -45)
  ladybug.forward(leg_lenght)
  n = n + 1

n=0
while (n < num_legs/2):
  ladybug.goto(0,-30)
  ladybug.setheading(distance_legs*n -45 +180)
  ladybug.forward(leg_lenght)
  n = n + 1
ladybug.setheading(0)
ladybug.penup()
ladybug.goto(0,0)
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(5)



# and body
ladybug.penup()
ladybug.goto(0,-55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

#don't mess with this
ladybug.hideturtle()
wn = trtl.Screen()
wn.mainloop()
