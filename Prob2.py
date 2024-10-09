########################################
# name: Sivana
# collaborators: collaborator's name (if any)
# estimated time spent (hrs): 45 mins
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    draws a pyramid of bricks centered on the screen. 
    """

    gw = GWindow(WIDTH, HEIGHT)

   
    start_x = (WIDTH - (BRICK_WIDTH * BRICKS_IN_BASE)) // 2
    start_y = HEIGHT - (BRICK_HEIGHT * (BRICKS_IN_BASE + 1)) // 2

    # draw the pyramid
    for row in range(BRICKS_IN_BASE):
        # number of bricks increases as we go up
        num_bricks = row + 1  

        # find the starting position for this row
        row_x = start_x + (BRICK_WIDTH * (BRICKS_IN_BASE - num_bricks)) // 2  # center the row
        row_y = start_y + (row * BRICK_HEIGHT)  # move down for each row

        # draw the bricks in this row
        for brick in range(num_bricks):
            brick_rect = GRect(row_x + (brick * BRICK_WIDTH), row_y, BRICK_WIDTH, BRICK_HEIGHT)
            brick_rect.setFilled(True)
            brick_rect.setFillColor("brown")  
            gw.add(brick_rect)

if __name__ == '__main__':
    draw_pyramid()
