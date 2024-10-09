########################################
# Name: Sivana
# Collaborators: collaborator's name (if any)
# Estimate time spent (hrs): about an hour 
########################################

from pgl import GWindow, GRect, GLabel
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():
    # set up the window
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    # create the square and center it
    square = GRect((GW_WIDTH - SQUARE_SIZE) // 2, (GW_HEIGHT - SQUARE_SIZE) // 2, SQUARE_SIZE, SQUARE_SIZE)
    square.setFilled(True)
    square.setFillColor("blue")  # pick a color
    gw.add(square)

    # initialize the score
    score = 0

    # create the score label to show just the number
    score_label = GLabel(f"{score}")
    score_label.setFont(SCORE_FONT)
    gw.add(score_label, SCORE_DX, GW_HEIGHT - SCORE_DY)

    # function to handle mouse clicks
    def on_mouse_down(event):
        nonlocal score  # use the outer score variable

        # check if the click is within the square
        if (square.getX() <= event.getX() <= square.getX() + SQUARE_SIZE and
            square.getY() <= event.getY() <= square.getY() + SQUARE_SIZE):
            # move the square to a random spot
            new_x = random.randint(0, GW_WIDTH - SQUARE_SIZE)
            new_y = random.randint(0, GW_HEIGHT - SQUARE_SIZE)
            square.setLocation(new_x, new_y)
            score += 1  # increase the score
        else:
            score = 0  # reset score if clicked outside

        # update the score label
        score_label.setLabel(f"{score}")

    # add the click event listener
    gw.addEventListener("click", on_mouse_down)

if __name__ == '__main__':
    clicky_box()
