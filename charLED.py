###
num = "0"
class charLED:
    
    digit_map = [
        [(0,-2), (1,-2), (2,-2), (3,-2)],
        [(0,-1), (1,-1), (2,-1), (3,-1)],
        [(0,0), (1,0), (2,0)],
        [(-1,1), (0,1), (1,1), (2,1)],
        [(-2,2), (-1,2), (0,2), (1,2)]
    ]
        
    char_map = {
    "0": [digit_map[0][0], digit_map[0][1], digit_map[1][0], digit_map[1][2], digit_map[3][1], digit_map[3][3], digit_map[4][2], digit_map[4][3]],
    "1": [digit_map[0][1], digit_map[1][1], digit_map[2][2], digit_map[3][2], digit_map[4][3]],
    "2": [digit_map[0][0], digit_map[0][1], digit_map[1][2], digit_map[2][1], digit_map[2][2], digit_map[3][1], digit_map[4][2], digit_map[4][3]],
    "3": [digit_map[0][0], digit_map[0][1], digit_map[1][2], digit_map[2][1], digit_map[2][2], digit_map[3][3], digit_map[4][2], digit_map[4][3]],
    "4": [digit_map[0][0], digit_map[1][0], digit_map[1][2], digit_map[2][0], digit_map[2][1], digit_map[2][2], digit_map[3][2], digit_map[4][3]],
    "5": [digit_map[0][0], digit_map[0][1], digit_map[1][0], digit_map[2][0], digit_map[2][1], digit_map[2][2], digit_map[3][3], digit_map[4][2], digit_map[4][3]],
    "6": [digit_map[0][1], digit_map[1][1], digit_map[2][1], digit_map[2][2], digit_map[3][1], digit_map[3][3], digit_map[4][2], digit_map[4][3]],
    "7": [digit_map[0][0], digit_map[0][1], digit_map[1][2], digit_map[2][2], digit_map[3][2], digit_map[4][2]],
    "8": [digit_map[0][0], digit_map[0][1], digit_map[1][0], digit_map[1][2], digit_map[2][1], digit_map[2][2], digit_map[3][1], digit_map[3][3], digit_map[4][2], digit_map[4][3]],
    "9": [digit_map[0][0], digit_map[0][1], digit_map[1][0], digit_map[1][2], digit_map[2][1], digit_map[2][2], digit_map[3][2], digit_map[4][2]]
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
            self.np[self.led_map[self.y + dy][self.x + dx]] = (255, 0, 0)
        self.np.write()