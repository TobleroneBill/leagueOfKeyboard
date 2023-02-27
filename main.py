import pyautogui
import keyboard

# TODO: This will be targeted towards MELEE champs, so need an array of 8 positions (maybe 9 if we include center)
# That can be used to reset the positions when a user gets out of position with AutoAiming

centerx, centery = pyautogui.size().width/2, pyautogui.size().height/2

enemyTestR = 'RedTest.png'

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
attackMode = True

#inputKeys = ('q','w','e','r','1','2','3','4','5','6')
inputKeys = ('q','w','e','r')

def UpdateScreenshot():
    global screenshot, xPos, yPos, enemyTestR
    # Mouse x and y, + AimAssist Range len + wid
    # x and y need to -= aimassist/2 to get this section of the screen
    rangeSizex = 500         # in Pixels
    rangeSizey = 600
    resolution = 2
    # Looks for health bar colors to target characters
    minionBar = (202,91,91)
    champBar = (154,37,27)

    xmin = int(xPos-(rangeSizex/2))
    xMax = int(rangeSizex)

    # TODO: need a system to dynamically size the Y axis. I think depending on the yPos (if above/below center apply
    # scalar to the yRange. Find percentage of screen that it is above center, and then yeah
    ymin = int(yPos-rangeSizey*1.3)
    yMax = int(rangeSizey * 2)

    sc = pyautogui.screenshot('img.png',region=(xmin,ymin,xMax,yMax))

    for x in range(0,sc.width,resolution):
        for y in range(0, sc.height, resolution):
            if sc.getpixel((x,y)) == champBar:
                xPos = xmin+x
                yPos = ymin+y

                if x > sc.width/2:
                    xPos += 50
                else:
                    xPos += 25
                yPos+= 100
                return

            if sc.getpixel((x,y)) == minionBar:
                xPos = xmin + x
                yPos = ymin + y

                if x > sc.width / 2:
                    xPos += 50
                else:
                    xPos += 25
                yPos += 100
                return

    print('heyo')


def ResetPos():
    global xPos,yPos
    xPos = centerx
    yPos = centery

# Changes the range into 3 states, Melee range,ADC range, and a middleground range that has ADC size but melee step
def SwapRange():
    print('_____________________________________________________')
    print('swapping')
    # Don't remember this being a requirement for stuff to work, but OK
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
            if yPos == yBot:
                yPos = yTop
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
            if yPos == yTop:
                yPos = yBot
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

    #keyboard.add_hotkey('space', lambda: UpdateScreenshot(),timeout=0)

    # Get Applies Autoaim for skills (against minions)
    for item in inputKeys:
        keyboard.add_hotkey(item, lambda: UpdateScreenshot(), timeout=0)


    # ____________________________Far Positions______________________________#
    # Makes Range smaller or bigger for ADC, vs Melee/.
    keyboard.add_hotkey('capslock',lambda: SwapRange())


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