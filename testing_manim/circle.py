from manim import *
from manim import Scene
class SquareToCircle(Scene):
    def construct(self):
        # Creating shapes
        circle = Circle()
        square = Square()

        #Showing shapes
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))