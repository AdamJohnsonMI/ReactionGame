from gpiozero import Button, LED, Buzzer
from time import time, sleep
from random import randint


led = LED(4)
buttonA = Button(15)
buttonB = Button(14)

score1 = 0
score2 = 0

print("\n\n\nWelcome to Adam's Reaction game")
print("The first player to three wins the game!")
print("Each side needs to hit their button first when the light turns on\n\n\n")

while (score1 < 3 and score2 < 3 ):
    print('Left player ' + str(score1) + ' - ' + 'Right player ' + str(score2))
    sleep(randint(1,10))
    led.on()
    def pressed(button):
        global score1
        global score2
        if button.pin.number == 14:
            print('Left player won the round')
            score1 += 1
        else:
            print('Right player won the round')
            score2 += 1
        led.off()
        if(score1==3):
            print("Left player wins the game!")
        elif(score2==3):
            print("Right player wins the game!")    
    buttonA.when_pressed = pressed
    buttonB.when_pressed = pressed
