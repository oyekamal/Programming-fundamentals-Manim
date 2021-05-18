from manim import *
import numpy as np
class DotMap(Scene):
    def construct(self):
        dots = dict()
        annos = dict()
        var_index = 0
        for x in range(-7, 8):
            for y in range(-4, 5):
                annos[f"{x}{y}"] = Text(f"({x}, {y})")
                dots[f"{var_index}"] = Dot(np.array([x, y, 0]))
                var_index = var_index + 1
        for anno, dot in zip(annos.values(), dots.values()):
            self.add(anno)
            self.add(dot)
            self.wait(0.2)
            self.remove(anno)