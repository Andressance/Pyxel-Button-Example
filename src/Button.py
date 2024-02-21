import pyxel
import math

class Button:
    def __init__(self, x, y, w, h, text, color_text, border_color, circle:bool ,blank:bool, hovered_text_color=None,hovered_color=None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color_text = color_text
        self.border_color = border_color
        self.circle = circle
        self.hovered_text_color = hovered_text_color
        self.hovered_color = hovered_color
        self.blank = blank
        
    def update(self) -> None:
        if self.hovered() and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            print("Button clicked")
            # Add your code here

    def draw(self) -> None:
        
        border_color = self.hovered_color if self.hovered() and self.hovered_color is not None else self.border_color
        text_color = self.hovered_text_color if self.hovered() and self.hovered_text_color is not None else self.color_text

        if self.circle:
            center = ((self.x + self.w) / 2, (self.y + self.h) / 2)
            if self.w == self.h:
                if self.blank:
                    pyxel.circb(self.x, self.y, self.w, border_color)
                else:
                    pyxel.circ(self.x, self.y, self.w, border_color)
                text_x, text_y = center[0] - 5, center[1] - 3
            else:
                self.draw_oval(self.x, self.y, self.w, self.h, border_color)
                text_x, text_y = center[0] - 5, center[1] - 3
        else:
            if self.blank:
                pyxel.rectb(self.x, self.y, self.w, self.h, border_color)
            else:
                pyxel.rect(self.x, self.y, self.w, self.h, border_color)
            text_x, text_y = self.x + 5, self.y + 5

        pyxel.text(text_x, text_y, self.text, text_color)


    def hovered(self) -> bool:
        if not self.circle:
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            return self.x < mx < self.x + self.w and self.y < my < self.y + self.h
        elif self.circle and self.w == self.h:
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            return (mx - self.x)**2 + (my - self.y)**2 < self.w**2
        elif self.circle and self.w != self.h:
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            return (mx - self.x)**2/self.w**2 + (my - self.y)**2/self.h**2 < 1
        
    def draw_oval(self, cx, cy, rx, ry, color):
        steps = 200  
        for i in range(steps):
            angle = (2 * math.pi / steps) * i
            x = cx + rx * math.cos(angle)
            y = cy + ry * math.sin(angle)
            pyxel.pset(x, y, color)  
        
    
