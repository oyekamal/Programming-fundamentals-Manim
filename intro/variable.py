from manim import *
import numpy as np

class displayText(Scene):
    def construct(self):
        # Create Text objects
        variable = Text('Variable')
        box = Text("lets create a Box name 'x'")
        veriable_x = Text('x', color=YELLOW_A)

        memory = Text("Memory", color=BLUE_E)

        code = Text("Code", color=BLUE_E)

        square = Square()

        vg = VGroup()
        memory.next_to(veriable_x, 2*UP)
        code.next_to(memory, 5*RIGHT)

        code_example = Tex("x"," = ", "2")

        

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
        self.play(ScaleInPlace(vg, 0.7))

        vg.generate_target()
        vg.target.move_to(3.5*LEFT)
        self.play(MoveToTarget(vg))

        self.play(ShowCreation(line))
        memory.to_corner(UL)
        code.next_to(memory, 18*RIGHT)

        # code.to_corner(UR, buff=3)
        self.play(FadeIn(memory),FadeIn(code))

        code_example.next_to(vg, 20*RIGHT)

        self.play(Write(code_example[0]))
        # b1 = Brace(code_example[0])
        brace = Brace(code_example[0], direction=DOWN)
        b1text = brace.get_text("Variable name").scale(0.7)
        self.add(brace,b1text)


        self.wait(2)