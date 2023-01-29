import pyautogui

class Cursor:

    centerWidth=0
    centerHeight=0

    def __init__(self, screenWidth, screenHeight) -> None:
        self.centerWidth = screenWidth/2
        self.centerHeight = screenHeight/2 - 200

    def movMause(self) -> None:
        pyautogui.moveTo(self.centerWidth, self.centerHeight, 1)
        pyautogui.moveTo(self.centerWidth + 200, self.centerHeight, 2) # Move the mouse to XY coordinates over 2 seconds.    
        pyautogui.moveTo(self.centerWidth + 200, self.centerHeight + 200, 2)
        pyautogui.moveTo(self.centerWidth, self.centerHeight + 200, 2)
        pyautogui.moveTo(self.centerWidth, self.centerHeight, 2)

def startIteration():
    screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
    # currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    cursor = Cursor(screenWidth, screenHeight)
    while True:
        cursor.movMause()

startIteration()

    
