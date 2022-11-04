from manim import *
from manim import Scene
class SquareToCircle(Scene):
    def construct(self):
        # Creating shapes
        circle = Circle()
        square = Square()

        #Showing shapes
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        mob = DashedLine(0.2*LEFT, 0.2*RIGHT,color= YELLOW)
        circ = Circle(stroke_color=YELLOW) 
        mob = DashedVMobject(circ, num_dashes=10) 

        self.play(Create(mob))
        self.wait(2)
