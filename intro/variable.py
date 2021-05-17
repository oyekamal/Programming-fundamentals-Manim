from manim import *


class displayText(Scene):
    def construct(self):
        # Create Text objects
        variable = Text('Variable')
        box = Text("lets create a Box name 'x'")
        veriable_x = Text('x', color=YELLOW_A)

        square = Square()

        vg = VGroup()
        # square.next_to(veriable_x, DOWN)

        START = (0,2.5,0)
        END =   (0,-2.5,0)
        line = Line(START,END)

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
        self.play(Rotate(square, PI/2))
        vg.add(veriable_x)
        vg.add(square)
        self.play(ScaleInPlace(vg, 0.5))

        vg.generate_target()
        vg.target.move_to(3*LEFT)
        self.play(MoveToTarget(vg))

        self.play(ShowCreation(line))


        

        self.wait(2)