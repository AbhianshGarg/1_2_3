#   a123_apple_1.py
from operator import index
import turtle as trtl
import random as rand

#-----setup-----
image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic('background.gif')
wn.addshape(image) # Make the screen aware of the new file
global drawer1, drawer2, drawer3, drawer4, drawer5
drawer1 = trtl.Turtle()
drawer2 = trtl.Turtle()
drawer3 = trtl.Turtle()
drawer4 = trtl.Turtle()
drawer5 = trtl.Turtle()

letter1 = trtl.Turtle()
letter2 = trtl.Turtle()
letter3 = trtl.Turtle()
letter4 = trtl.Turtle()
letter5 = trtl.Turtle()

index = 0
xcor = -200

#-----functions-----

# This function takes care of font and color.

def take_turtle(drawer, draw_letter):
  global index, xcor
  draw_letter.penup()
  draw_letter.goto(xcor, 120)

  xcor += 70
  draw_letter.color("white")
  draw_letter.write(letter[index], font=("Arial", 74, "bold")) 
  index += 1

  drawer.shape(image)
  rand_x = rand.randint(-200, 200)
  rand_y = rand.randint(-200, 200)
  drawer.penup()
  drawer.goto(rand_x, rand_y)
  drawer.pendown()
  return drawer

def get_letter():
  dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  letter_list = []
  for i in range(5):
    letter = dictionary[rand.randint(0, 25)]
    letter_list.append(letter)
  return letter_list

def draw_a_letter(letter, drawer):
  drawer.color("white")
  drawer.write(letter, font=("Arial", 74, "bold")) 


# given a turtle, set that turtle to be shaped by the image file
def draw_apple1():
  drawer1.penup()
  drawer1.goto(0, -200)
  drawer1.pendown()
  wn.update() 

def draw_apple2():
  drawer2.penup()
  drawer2.goto(0, -200)
  drawer2.pendown()
  wn.update() 

def draw_apple3():
  drawer3.penup()
  drawer3.goto(0, -200)
  drawer3.pendown()
  wn.update() 

def draw_apple4():
  drawer4.penup()
  drawer4.goto(0, -200)
  drawer4.pendown()
  wn.update() 
  
def draw_apple5():
  drawer5.penup()
  drawer5.goto(0, -200)
  drawer5.pendown()
  wn.update()   

#-----function calls-----
global letter
letter = get_letter()
print(letter)

drawer1 = take_turtle(drawer1, letter1)
drawer2 = take_turtle(drawer2, letter2)
drawer3 = take_turtle(drawer3, letter3)
drawer4 = take_turtle(drawer4, letter4)
drawer5 = take_turtle(drawer5, letter5)

wn.onkeypress(draw_apple1, letter[0])
wn.onkeypress(draw_apple2, letter[1])
wn.onkeypress(draw_apple3, letter[2])
wn.onkeypress(draw_apple4, letter[3])
wn.onkeypress(draw_apple5, letter[4])


wn.listen()
wn.mainloop()
