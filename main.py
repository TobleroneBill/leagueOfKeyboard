import pyautogui
import keyboard



centerx, centery = pyautogui.size().width/2, pyautogui.size().height/2



movementSizeMax = centerx/2.5
movementSizestep = movementSizeMax/2
movementSize = movementSizeMax

ADCRange = movementSizeMax
MeleeRange = movementSizeMax/2



xRight = centerx + movementSizeMax
xLeft = centerx - movementSizeMax
yBot = centery + movementSizeMax
yTop = centery - movementSizeMax


xPos = centerx
yPos = centery

toggleCenter = False
meleeADCNormalSwitch = 0



def ResetPos():
    global xPos,yPos
    xPos = centerx
    yPos = centery



# Changes the range into 3 states, Melee range,ADC range, and a middleground range that has ADC size but melee step
def SwapRange():
    print('_____________________________________________________')
    print('swapping')
    global meleeADCNormalSwitch, movementSizeMax, movementSizestep ,xRight,xLeft,yBot,yTop, centerx
    meleeADCNormalSwitch += 1
    if meleeADCNormalSwitch > 2:
        meleeADCNormalSwitch = 0

    print(f'range ={meleeADCNormalSwitch}')
    if meleeADCNormalSwitch == 0:
        movementSizestep = MeleeRange
        movementSizeMax = MeleeRange
    elif meleeADCNormalSwitch == 1:
        movementSizestep = ADCRange
        movementSizeMax = ADCRange
    elif meleeADCNormalSwitch == 2:
        movementSizestep = movementSizeMax / 2
        movementSizeMax = centerx / 2.5

    xRight = centerx + movementSizeMax
    xLeft = centerx - movementSizeMax
    yBot = centery + movementSizeMax
    yTop = centery - movementSizeMax

    print(f'Step size: {movementSizestep}')
    print(f'maxMove = {movementSizeMax}')
    ResetPos()

def print_hi():
    print('hi')

def MouseToKey(key):
    global toggleCenter,yPos,xPos

    print(f'Key Pressed: {key}')


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
                if yPos < centery:
                    yPos += movementSizestep
                if yPos > centery:
                    yPos -= movementSizestep
            if xPos > xLeft:
                newPos = xPos - movementSizestep
                xPos = newPos
        case 'right':
            if xPos == xRight:
                if yPos < centery:
                    yPos += movementSizestep
                if yPos > centery:
                    yPos -= movementSizestep
            if xPos < xRight:
                newPos = xPos + movementSizestep
                xPos = newPos

    # ____________________________Far Positions______________________________#
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
    #____________________________Close Positions______________________________#
    keyboard.add_hotkey('up',lambda: MouseToKey('up'),timeout=0)
    keyboard.add_hotkey('up + left',lambda: MouseToKey('upLeft'),timeout=0)
    keyboard.add_hotkey('up + Right',lambda: MouseToKey('upRight'),timeout=0)

    keyboard.add_hotkey('down',lambda: MouseToKey('down'),timeout=0)
    keyboard.add_hotkey('down + left',lambda: MouseToKey('downleft'),timeout=0)
    keyboard.add_hotkey('down + right',lambda: MouseToKey('downright'),timeout=0)


    keyboard.add_hotkey('left', lambda: MouseToKey('left'),timeout=0)
    keyboard.add_hotkey('right', lambda: MouseToKey('right'),timeout=0)
    keyboard.add_hotkey('m', lambda: MouseToKey('right alt'),timeout=0)

    # ____________________________Far Positions______________________________#
    # Makes Range smaller or bigger for ADC, vs Melee/.
    keyboard.add_hotkey('capslock',lambda: SwapRange())

    # Use if you want a worse experience
    '''
    keyboard.add_hotkey('up+shift',lambda: MouseToKey('upshift'),timeout=0)
    keyboard.add_hotkey('down+shift',lambda: MouseToKey('downshift'),timeout=0)

    keyboard.add_hotkey('left+shift',lambda: MouseToKey('leftshift'),timeout=0)
    keyboard.add_hotkey('right+shift',lambda: MouseToKey('rightshift'),timeout=0)
    '''


    # I fucking hate this janky shitty module MAKE A BETTER THING omzomgroemageinrgaleijrgalerglahrelkaheroa
    Toggle = True

    def invertToggle():
        global Toggle
        Toggle = not Toggle
        print(f'LockedMouse: {Toggle}')

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
            print("Mouse Centered")
            ResetPos()