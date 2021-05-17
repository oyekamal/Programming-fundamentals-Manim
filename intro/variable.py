from manim import *


class displayText(Scene):
    def construct(self):
        # Create Text objects
        variable = Text('Variable')

        box = Text("lets create a Box name 'x'")

        veriable_x = Text('x', color=YELLOW_A)


        # Displaying text
        self.wait(1)
        self.play(Write(variable))
        self.wait(1)
        self.play(ReplacementTransform(variable, box))
        self.wait(1)
        self.play(ReplacementTransform(box, veriable_x))
        self.wait(2)