"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zhengshan "bill" fang.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
roof= rg.SimpleTurtle()
roof.pen = rg.Pen('midnight blue', 3)
roof.speed=1114000000
roof.pen_up()

roof.go_to(rg.Point(-30,-180))

roof.pen_down()

for k in range(12):
    roof.forward(100)
    roof.left(120)
    roof.forward(100)
    roof.left(120)
    roof.forward(100)
    roof.left(30)
    roof.forward(100)
    roof.left(90)
    roof.forward(40)
    roof.draw_regular_polygon(4,20)
    roof.forward(60)
    roof.left(90)
    roof.forward(100)
    roof.right(60)

# window = rg.TurtleWindow()
qwe= rg.SimpleTurtle()
qwe.pen = rg.Pen('red', 3)
qwe.speed=1114
qwe.pen_up()
qwe.go_to(rg.Point(-30,-180))
qwe.pen_down()
for k in range(12):
    qwe.pen_up()
    qwe.forward(100)
    qwe.pen_down()

    qwe.left(90)
    qwe.forward(100)
    qwe.left(90)
    qwe.forward(20)
    qwe.left(90)
    qwe.forward(100)
    qwe.left(90)
    qwe.forward(20)

    qwe.left(30)

window.close_on_mouse_click()