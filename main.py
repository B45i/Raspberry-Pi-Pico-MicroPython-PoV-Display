from machine import Pin
import time

leds = [Pin(x, Pin.OUT) for x in range(5)]

for led in leds:
    led.value(0)

# Generated using: https://pov-display-calc.vercel.app/
# Source: https://github.com/B45i/pov-display-calc
alphabets = [
    [30, 5, 5, 30, 0],
    [31, 21, 21, 10, 0],
    [14, 17, 17, 10, 0],
    [31, 17, 17, 14, 0],
    [31, 21, 21, 17, 0],
    [31, 20, 20, 16, 0],
    [14, 17, 19, 10, 0],
    [31, 4, 4, 4, 31],
    [0, 17, 31, 17, 0],
    [0, 17, 30, 16, 0],
    [31, 4, 10, 17, 0],
    [31, 1, 1, 1, 0],
    [31, 12, 3, 12, 31],
    [31, 12, 3, 31, 0],
    [14, 17, 17, 14, 0],
    [31, 20, 20, 8, 0],
    [14, 17, 19, 14, 2],
    [31, 20, 22, 9, 0],
    [8, 21, 21, 2, 0],
    [16, 16, 31, 16, 16],
    [30, 1, 1, 30, 0],
    [24, 6, 1, 6, 24],
    [28, 3, 12, 3, 28],
    [17, 10, 4, 10, 17],
    [17, 10, 4, 8, 16],
    [19, 21, 21, 25, 0],
    ]


def display_line(line):
    global leds
    print(line)

    if line >= 16:
        leds[0].value(1)
        line -= 16
    else:
        leds[0].value(0)

    if line >= 8:
        leds[1].value(1)
        line -= 8
    else:
        leds[1].value(0)

    if line >= 4:
        leds[2].value(1)
        line -= 4
    else:
        leds[2].value(0)

    if line >= 2:
        leds[3].value(1)
        line -= 2
    else:
        leds[3].value(0)

    if line >= 1:
        leds[4].value(1)
        line -= 1
    else:
        leds[4].value(0)


def display_letter(char):
    for c in char:
        display_line(c)
    display_line(0)


def display_string(s):
    global alphabets
    for c in list(s.upper()):
        display_letter(alphabets[ord(c) - 91])
        time.sleep(.008)


while True:
    display_string('Hello')
