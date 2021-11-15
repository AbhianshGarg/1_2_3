#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic('background.gif')
wn.addshape(image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()

#-----functions-----

# This function takes care of font and color.
def get_letter():
  dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  letter = dictionary[rand.randint(0, 25)]
  print(letter)
  return letter

def draw_an_letter(letter):
  drawer.color("white")
  drawer.write(letter, font=("Arial", 74, "bold")) 

def move_apple():
  apple.penup()
  apple.goto(0, -200)
  apple.pendown()
  drawer.clear()

def reset_apple():
  apple.hideturtle()
  apple.penup()
  apple.goto(0, 0)
  apple.pendown()
  apple.showturtle()

# given a turtle, set that turtle to be shaped by the image file
def draw_apple():
  apple.shape(image)
  move_apple()
  reset_apple()
  wn.update()

#-----function calls-----

letter = get_letter()
draw_an_letter(letter.upper())
wn.onkeypress(draw_apple, letter)

wn.listen()
wn.mainloop()