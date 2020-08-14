from sense_hat import *
import time
sense = SenseHat()

# def gatherTemp():
temp = (sense.get_temperature() - 18)

# def convertTemp(temp):
floatTemp = float(temp)
roundedTemp = round(temp, 1)
tempMessage = str(roundedTemp) + 'c'

def displayTemp():
    #currently not implemented, makes it wait for button press
#     activateTemp = sense.stick.wait_for_event(emptybuffer = True)
    temp = (sense.get_temperature() - 18)
    floatTemp = float(temp)
    roundedTemp = round(temp, 1)
    tempMessage = str(roundedTemp) + 'c'
    while roundedTemp >= 22:
        temp = (sense.get_temperature() - 18)
        floatTemp = float(temp)
        roundedTemp = round(temp, 1)
        tempMessage = str(roundedTemp) + 'c'
        if roundedTemp >= 22:
            sense.show_message('TOO HOT: ' + tempMessage, scroll_speed = (0.05), text_colour = (255,0,0), back_colour = (0, 0, 0))
            break
        else:
            sense.show_message(tempMessage, scroll_speed = (0.09), text_colour = (200,0,200), back_colour = (0, 0, 200))
            sense.clear
    
def displayHamster():
    b = (156, 95, 65) #brown
    lb = (204, 140, 108) #light brown
    p = (255, 120, 140) #pink for ears and nose
    lp = (248, 187, 208) #light pink for mouth
    w = (255, 255, 255) #white
    bl = (0, 0, 0) #black/empty
    


#Creates the 1st hamster
    hamster1 = [
        b, b, b, bl, bl, b, b, b,
        b, p, b, bl, bl, b, p, b,
        b, b, b, b, b, b, b, b,
        bl, b, bl, b, b, bl, b, bl,
        b, b, bl, b, b, bl, b, b,
        b, b, b, b, b, b, b, b,
        b, lp, lp, p, p, lp, lp, b,
        bl, lp, lp, lp, lp, lp, lp, bl
        ]
    
#Creates the 2nd hamster    
    hamster2 = [
        b, b, b, bl, bl, b, b, b,
        b, p, b, bl, bl, b, p, b,
        b, b, b, b, b, b, b, b,
        bl, b, lb, b, b, lb, b, bl,
        b, b, bl, b, b, bl, b, b,
        b, b, b, b, b, b, b, b,
        b, lp, lp, p, p, lp, lp, b,
        bl, lp, lp, lp, lp, lp, lp, bl
        ]
    
    #Creates the 3rd hamster
    hamster3 = [
        b, b, b, bl, bl, b, b, b,
        b, p, b, bl, bl, b, p, b,
        b, b, b, b, b, b, b, b,
        bl, b, lb, b, b, lb, b, bl,
        b, b, bl, b, b, bl, b, b,
        b, lp, lp, p, p, lp, lp, b,
        b, lp, lp, lp, lp, lp, lp, b,
        bl, b, b, b, b, b, b, bl
        ]

    
    sense.set_pixels(hamster1)
    time.sleep(1.5)
    sense.set_pixels(hamster2)
    time.sleep(1.5)
    sense.set_pixels(hamster3)
    time.sleep(1.5)
    sense.set_pixels(hamster1)
    time.sleep(1.5)
 
while True:
    displayHamster()
    displayTemp()
    
    #Not currently implemented, this is to change the event to wait for a button press
#     event = sense.stick.wait_for_event()
#     if event.action == ACTION_PRESSED:
#         displayTemp()
#     sense.clear()
    
