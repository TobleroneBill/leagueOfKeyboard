import pyautogui
import keyboard

movementSizeMax = 400
movementSizestep = 200
movementSize = movementSizeMax


centerx, centery = pyautogui.size().width/2, pyautogui.size().height/2

xRight = centerx + movementSizeMax
xLeft = centerx - movementSizeMax

yBot = centery + movementSizeMax
yTop = centery - movementSizeMax


xPos = centerx
yPos = centery

toggleCenter = False

def ResetPos():
    global xPos,yPos
    xPos = centerx
    yPos = centery

def print_hi():
    print('hi')

def MouseToKey(key):
    global toggleCenter,yPos,xPos

    match key:
    #____________________________Far Positions______________________________#
        case 'upLeft':
            if yPos > yTop:
                newPos = yPos - movementSizestep
                yPos = newPos
            if xPos > xLeft:
                newPos = xPos - movementSizestep
                xPos = newPos
        case 'upRight':
            if yPos > yTop:
                newPos = yPos - movementSizestep
                yPos = newPos
            if xPos < xRight :
                newPos = xPos + movementSizestep
                xPos = newPos
        case 'up':
            # Order Matters
            if yPos == yTop:
                if xPos < centerx:
                    xPos += movementSizestep
                if xPos > centerx:
                    xPos -= movementSizestep
            if yPos > yTop:
                newPos = yPos - movementSizestep
                yPos = newPos



        case 'downleft':
            if yPos < yBot:
                newPos = yPos + movementSizestep
                yPos = newPos
            if xPos > xLeft:
                newPos = xPos - movementSizestep
                xPos = newPos
        case 'downright':
            if yPos < yBot:
                newPos = yPos + movementSizestep
                yPos = newPos
            if xPos < xRight:
                newPos = xPos + movementSizestep
                xPos = newPos

        case 'down':
            if yPos == yBot:
                if xPos < centerx:
                    xPos += movementSizestep
                if xPos > centerx:
                    xPos -= movementSizestep
            if yPos < yBot:
                newPos = yPos + movementSizestep
                yPos = newPos

        case 'left':
            if xPos == xLeft:
                yPos = centery
            if xPos > xLeft:
                newPos = xPos - movementSizestep
                xPos = newPos
        case 'right':
            if xPos == xRight:
                yPos = centery
            if xPos < xRight:
                newPos = xPos + movementSizestep
                xPos = newPos

    # ____________________________Close Positions______________________________#
        # because of my bad inital setup, of getting each needed key as a hot key
        # This has to be done the long way. Ideally I would just have a HalfSize boolean that gets toggled if
        # shift is pressed.
        # If this gets any bigger, I will have to figure something out or do this in c++
        case 'upshift':
            # Order Matters
            if yPos == yTop:
                xPos = centerx
            if yPos > yTop:
                newPos = yPos - (movementSizestep*2)
                yPos = newPos

        case 'downshift':
            if yPos == yBot:
                xPos = centerx
            if yPos < yBot:
                newPos = yPos + (movementSizestep*2)
                yPos = newPos

        case 'leftshift':
            if xPos == xLeft:
                yPos = centery
            if xPos > xLeft:
                newPos = xPos - (movementSizestep*2)
                xPos = newPos

        case 'rightshift':
            if xPos == xLeft:
                yPos = centery
            if xPos > xLeft:
                newPos = xPos + (movementSizestep*2)
                xPos = newPos

        case 'right alt':
            print('OK')
            toggleCenter = not toggleCenter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    #____________________________Far Positions______________________________#
    keyboard.add_hotkey('up',lambda: MouseToKey('up'),timeout=0)
    keyboard.add_hotkey('up + left',lambda: MouseToKey('upLeft'),timeout=0)
    keyboard.add_hotkey('up + Right',lambda: MouseToKey('upRight'),timeout=0)

    keyboard.add_hotkey('down',lambda: MouseToKey('down'),timeout=0)
    keyboard.add_hotkey('down + left',lambda: MouseToKey('downleft'),timeout=0)
    keyboard.add_hotkey('down + right',lambda: MouseToKey('downright'),timeout=0)


    keyboard.add_hotkey('left', lambda: MouseToKey('left'),timeout=0)
    keyboard.add_hotkey('right', lambda: MouseToKey('right'),timeout=0)
    keyboard.add_hotkey('m', lambda: MouseToKey('right alt'),timeout=0)

    # ____________________________Close Positions______________________________#
    keyboard.add_hotkey('up+shift',lambda: MouseToKey('upshift'),timeout=0)
    keyboard.add_hotkey('down+shift',lambda: MouseToKey('downshift'),timeout=0)

    keyboard.add_hotkey('left+shift',lambda: MouseToKey('leftshift'),timeout=0)
    keyboard.add_hotkey('right+shift',lambda: MouseToKey('rightshift'),timeout=0)


    invertBool = lambda g: not g

    # I fucking hate this janky shitty module MAKE A BETTER THING omzomgroemageinrgaleijrgalerglahrelkaheroa
    Toggle = True

    def invertToggle():
        global Toggle
        Toggle = not Toggle

    keyboard.add_hotkey('/', invertToggle)

    gaming = True

    def invertGaming():
        global gaming
        gaming = not gaming

    keyboard.add_hotkey('`',invertGaming)

    while (gaming):
        if Toggle:
            pyautogui.moveTo(xPos, yPos)

        if keyboard.is_pressed('right control'):
            print("ok")
            ResetPos()