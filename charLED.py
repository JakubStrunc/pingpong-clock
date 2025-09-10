class charLED:
    
    char_map = {
    "0": [(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(2,2),(0,3),(2,3),(0,4),(1,4),(2,4)],
    "1": [(0,2),(-1,1)],
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
        print(coords)

        if not coords:
            print("error")
        
        for dx, dy in coords:
            self.np[self.led_map[self.y + dy][self.x + dx]] = (255, 0, 0)
        self.np.write()

        

    


