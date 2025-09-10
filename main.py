import machine, neopixel, time
from machine import Pin
# from charLED import charLED

NUM_LEDS = 128  # počet LED na pásku
PIN = 2    # GPIO pin (GP2)

np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)



# led map make
LED_MAP = [
    [12, 13, 26, 27, 40, 41, 54, 55, 68, 69, 82, 83, 96, 97, 110, 111, 124],
    [1, 11, 14, 25, 28, 39, 42, 53, 56, 67, 70, 81, 84, 95, 98, 109, 112, 123],
    [2, 10, 15, 24, 29, 38, 43, 52, 57, 66, 71, 80, 85, 94, 99, 108, 113, 122, 125],
    [0, 3, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93, 100, 107, 114, 121, 126],
    [4, 8, 17, 22, 31, 36, 45, 50, 59, 64, 73, 78, 87, 92, 101, 106, 115, 120, 127],
    [5, 7, 18, 21, 32, 35, 46, 49, 60, 63, 74, 77, 88, 91, 102, 105, 116, 119],
    [6, 19, 20, 33, 34, 47, 48, 61, 62, 75, 76, 89, 90, 103, 104, 117, 118]
  
]

###

class charLED:
    
    char_map = {
    "0": [(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(2,2),(0,3),(2,3),(0,4),(1,4),(2,4)],
    "1": [(0,0),(-1,1),[-1,-1],[-1,-2],[-1,2]],
    "2": [(0,0),(1,0),(2,0),(2,1),(1,2),(0,3),(0,4),(1,4),(2,4)]
    }
    def __init__(self, x, y, np, led_map):
        self.x = x  # levý horní roh znaku
        self.y = y
        self.np = np
        self.led_map = led_map

    
    def draw(self, char):
        """vykreslí znak na pozici (x,y)"""
        char = str(char)
        
        coords = self.char_map.get(char)
        # print(coords)

        if not coords:
            print("error")
        
        for dx, dy in coords:
            print(self.y + dy, self.x + dx)
            self.np[self.led_map[self.y + dy][self.x + dx]] = (255, 0, 0)
        self.np.write()

pin = Pin("LED", Pin.OUT)

char = charLED(3, 3, np, LED_MAP)

def clear():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()


while True:
    try:
        # pin.toggle()
        # # Červená
        # print("red")
        # for i in range(NUM_LEDS):
        #     np[i] = (60, 0, 0)
        # np.write()
        # time.sleep(1)

        # # Zelená
        # print("green")
        # for i in range(NUM_LEDS):
        #     np[i] = (0, 60, 0)
        # np.write()
        # time.sleep(1)

        # # Modrá
        # print("blue")
        # for i in range(NUM_LEDS):
        #     np[i] = (0, 0, 60)
        # np.write()
        # time.sleep(1)
        print("working")
        char.draw("1")

        # clear()
        # for line in LED_MAP:
        #     for led in line:
        #         np[led] = (255, 0, 0)
        #         np.write()
        #         time.sleep(0.25)
                

    except KeyboardInterrupt:
        break

clear()
pin.off()
print("konec")


