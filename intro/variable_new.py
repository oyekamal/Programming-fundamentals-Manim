from manim import *
import numpy as np


class Variable(Scene):
    def construct(self):
        # Create objects
        variable = Text('Variable')

        num = Text('25')
        num_box = always_redraw(lambda: SurroundingRectangle(
            num, buff=1))
        num_box_name = always_redraw(lambda: Tex(
            "age", color=GREEN).next_to(num_box, UP, buff=0.5))

        # play the objects

        # box num_box
        self.play(Create(num_box))
        self.play(Rotate(num_box, PI))
        self.wait()
        self.play(Write(num_box_name))
        self.play(FadeIn(num))
        self.wait()
        self.play(num.animate.shift(LEFT*5))
        self.wait()
