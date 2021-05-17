from manim import *


class displayText(Scene):
    def construct(self):
        # Create Text objects
        variable = Text('Variable')
        box = Text("lets create a Box name 'x'")
        veriable_x = Text('x', color=YELLOW_A)

        square = Square()

        # square.next_to(veriable_x, DOWN)

        # Displaying text
        self.wait(1)
        self.play(Write(variable))
        self.wait(1)
        self.play(ReplacementTransform(variable, box))
        self.wait(1)
        self.play(ReplacementTransform(box, veriable_x))
        self.wait(2)

        veriable_x.generate_target()
        veriable_x.target.move_to(2*UP)
        self.play(MoveToTarget(veriable_x))

        square.next_to(veriable_x, DOWN)
        # square.shift(2 * DOWN)
        self.play(ShowCreation(square))
        self.wait(2)