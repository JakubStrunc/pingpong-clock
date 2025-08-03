import machine, neopixel, time
from machine import Pin

NUM_LEDS = 60  # počet LED na pásku
PIN = 2    # GPIO pin (GP2)

np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

pin = Pin("LED", Pin.OUT)
while True:
    try:
        pin.toggle()
        # Červená
        print("red")
        for i in range(NUM_LEDS):
            np[i] = (255, 0, 0)
        np.write()
        time.sleep(1)

        # Zelená
        print("green")
        for i in range(NUM_LEDS):
            np[i] = (0, 255, 0)
        np.write()
        time.sleep(1)

        # Modrá
        print("blue")
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 255)
        np.write()
        time.sleep(1)

    except KeyboardInterrupt:
        break

pin.off()
print("konec")


