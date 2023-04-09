from turtle import*
#function for curve
def curve01(a,d):
 for i in range(d):
  right(a)
  forward(1)
def curve02(a,d):
 for i in range(d):
  left(a)
  forward(1)

penup()
forward(600)
pendown()
left(90)
#WHITE SIDE
forward(400)
left(90)
forward(1200)
left(90)
forward(800)
left(90)
forward(1200)
left(90)
fd(400)
back(400)
right(90)
back(600)
#GREEN SIDE
fillcolor("#006633")
begin_fill()
left(90)
forward(800)
left(90)
forward(600)
left(90)
forward(800)
left(90)
forward(600)
end_fill()
penup()
left(71.1)
forward(532)
pendown()
left(60)
#CRESCENT SHAPE
fillcolor("#D21034")
begin_fill()
curve02(0.35,380)
curve02(0.37,288)
curve02(0.29,118)
right(167)
curve01(0.25,85)
curve01(0.3,250)
curve01(0.25,190)
right(5)
curve01(0.29,330)
curve01(0.23,95)
curve01(0.35,98)
end_fill()
penup()
right(112.5)
forward(63.5)
left(50)
pendown()
#STAR
fillcolor("#D21034")
begin_fill()
forward(72)
right(74)
forward(73)
left(145)
forward(73)
right(74)
forward(73)
left(145)
forward(73)
right(71)
forward(73)
left(144.5)
forward(73)
right(72.5)
forward(74)
left(145)
forward(73)
right(73.5)
forward(73)
end_fill()

done()