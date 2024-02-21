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

if __name__ == "__main__":
    App()
