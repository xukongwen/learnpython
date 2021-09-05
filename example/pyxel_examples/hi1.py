import pyxel


class App:
   
    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)


App()
