import pyxel
from Button import Button

class App:
    def __init__(self) -> None:
        pyxel.init(80, 80)
        pyxel.mouse(True)
        self.button = Button(20, 10, 30, 15, "Button", 1 , 7, False, False, None, 6) # Example of a button
        pyxel.run(self.update, self.draw)
        

    def update(self) -> None:
        self.button.update()

    def draw(self) -> None:
        pyxel.cls(0)
        self.button.draw()
        
        pyxel.text(5, 5, "Click the button", 7)
        if self.button.is_clicked():
            pyxel.text(5, 15, "Button clicked!", 8)
        else:
            pyxel.text(5, 15, "Button not clicked", 7)

        pyxel.text(5, 25, "Mouse position: ({}, {})".format(pyxel.mouse_x, pyxel.mouse_y), 7)
        
        pyxel.text(5, 35, "Mouse button pressed: {}".format(pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)), 7)

if __name__ == "__main__":
    App()
