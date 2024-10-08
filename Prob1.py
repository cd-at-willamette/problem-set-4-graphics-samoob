############################################################
# Name: Sivana
# Name(s) of anyone worked with:
# Est time spent (hr): 2
############################################################
from pgl import GWindow, GRect, GOval, GLine, GLabel


WIDTH = 400
HEIGHT = 400

def draw_image():
    """ creates a window and draws a whimsical scene """

    # create the window
    gw = GWindow(WIDTH, HEIGHT)

    # draw the sky (light blue rectangle)
    sky = GRect(0, 0, WIDTH, HEIGHT // 2)
    sky.setFilled(True)
    sky.setFillColor("lightblue")
    gw.add(sky)

    # draw the ground (green rectangle)
    ground = GRect(0, HEIGHT // 2, WIDTH, HEIGHT // 2)
    ground.setFilled(True)
    ground.setFillColor("green")
    gw.add(ground)

    # draw some clouds 
    cloud1 = GOval(50, 30, 80, 40)
    cloud1.setFilled(True)
    cloud1.setFillColor("white")
    gw.add(cloud1)

    cloud2 = GOval(250, 50, 100, 50)
    cloud2.setFilled(True)
    cloud2.setFillColor("white")
    gw.add(cloud2)

    # draw a rainbow thing also pride yass
    for i in range(7):
        arc = GOval(-100 + i * 20, 120, 600 - i * 40, 300 - i * 30)
        arc.setFilled(False)
        arc.setColor(["red", "orange", "yellow", "green", "blue", "indigo", "violet"][i])
        gw.add(arc)

    # draw the castle (rectangles and triangles)
    castle_body = GRect(150, 200, 100, 100)
    castle_body.setFilled(True)
    castle_body.setFillColor("lightgrey")
    gw.add(castle_body)

    tower1 = GRect(130, 150, 40, 80)
    tower1.setFilled(True)
    tower1.setFillColor("darkgrey")
    gw.add(tower1)

    tower2 = GRect(230, 150, 40, 80)
    tower2.setFilled(True)
    tower2.setFillColor("darkgrey")
    gw.add(tower2)

    # draw the roofs yes they supposed to look weird 
    roof1 = GLine(150, 200, 130, 150)  # left roof
    gw.add(roof1)
    roof1 = GLine(170, 150, 130, 150)
    gw.add(roof1)

    roof2 = GLine(250, 200, 270, 150)  # right roof
    gw.add(roof2)
    roof2 = GLine(230, 150, 270, 150)
    gw.add(roof2)

    # draw a door (rectangle)
    door = GRect(190, 250, 20, 50)
    door.setFilled(True)
    door.setFillColor("brown")
    gw.add(door)

    # add a label
    label = GLabel("a magical land!")
    label.setFont("Arial-24")  # keep the original font setting
    label.setColor("black")
    gw.add(label, 130, 50)

if __name__ == '__main__':
    draw_image()
