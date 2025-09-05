from OpenGL.GL import * # Has all the main drawing commands (draw shapes, set colors, etc.).
from OpenGL.GLUT import * #Helps create windows and handle things like mouse/keyboard input.
from OpenGL.GLU import * #Has helper functions for setting up the camera and perspective.

w,h= 500,500

# ---Section 1--- ** changes to be brought in this only **
def square():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the corner 
    glVertex2f(100, 100) # Coordinates for the bottom left point
    glVertex2f(200, 100) # Coordinates for the bottom right point
    glVertex2f(200, 200) # Coordinates for the top right point
    glVertex2f(100, 200) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

# ---Section 2---

def iterate():
    glViewport(0, 0, h, w) # # Set the part of the window to draw in (here, the whole window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) ## Set a flat 2D view from (0,0) to (500,500)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity() ## Reset again before drawing

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    iterate() # Set up the view again
    glColor3f(1.0, 0.0, 3.0)  # Set the color to pink
    square() # Draw a square using our function
    glutSwapBuffers() # Show the new frame on screen

glutInit() # Start GLUT
glutInitDisplayMode(GLUT_RGBA) # Window will support Red, Green, Blue, Alpha (transparency)
glutInitWindowSize(w, h)   # Set window size
glutInitWindowPosition(0, 0)   # Put window at top-left of the screen
wind = glutCreateWindow(b"OpenGL Coding Practice - Simple Square") # Create window with title
glutDisplayFunc(showScreen) # When window needs to draw, call showScreen()
glutIdleFunc(showScreen) # When idle, keep calling showScreen() so it keeps updating
glutMainLoop() # Start the event loop (never ends until you close window)