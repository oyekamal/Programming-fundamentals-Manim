from manim import *
import numpy as np

class displayText(Scene):
    def construct(self):
        # Create Text objects
        variable = Text('Variable')
        box = Text("lets create a Box name 'x'")
        veriable_x = Text('x', color=YELLOW)
        

        memory = Text("Memory", color=BLUE_E)

        code = Text("Code", color=BLUE_E)

        two = Text("2",color=RED)
        five = Text("5",color=RED)
        two.move_to(np.array([-1.5,2,0]))
        # two.move_to(2*UP)
        square = Square()

        vg = VGroup()
        memory.next_to(veriable_x, 2*UP)
        code.next_to(memory, 5*RIGHT)

        code_example = Tex("x"," = ", "2", " + ", "3")
        code_example[0].set_color(YELLOW)
        code_example[2].set_color(RED)

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
        # self.play(Rotating(square))

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

        self.play(Write(two))


        curvedArrow=CurvedArrow(start_point=np.array([-1.8,2,0]),end_point=np.array([-3,0.6,0]))
        self.play(ShowCreation(curvedArrow))
        self.wait()


        self.play(Write(code_example[0]))
        # b1 = Brace(code_example[0])
        brace_x = Brace(code_example[0], direction=DOWN)
        b1text_x = brace_x.get_text("Variable name").scale(0.7)
        
        self.play(Write(code_example[1]))

        brace_ = Brace(code_example[1], direction=UP)
        b1text_ = brace_.get_text("assignmet").scale(0.7).set_color(GREEN)


        brace_value = Brace(code_example[2], direction=RIGHT)
        b1text_value = brace_value.get_text("value").scale(0.7).set_color(RED)



        self.play(ShowCreation(brace_x),Write(b1text_x), ShowCreation(brace_),Write(b1text_))

        self.play(Write(code_example[2]))

        self.play(ShowCreation(brace_value),Write(b1text_value))


        self.play(FadeOutAndShift(b1text_x, DOWN),FadeOutAndShift(brace_x, DOWN),
                  FadeOutAndShift(b1text_value, RIGHT),FadeOutAndShift(brace_value, RIGHT),
                  FadeOutAndShift(b1text_, UP),FadeOutAndShift(brace_, UP),)
        self.remove(b1text_x, brace_x, b1text_, brace_, b1text_value, brace_value)
        
        
        self.play(FadeOut(curvedArrow))
        
        two.generate_target()
        two.target.move_to(square.get_center())
        self.play(MoveToTarget(two))
        
        five.move_to(square.get_center())
        
        
        self.play(Write(code_example[3]),Write(code_example[4]))
        
        self.play(ReplacementTransform(two, five))

        self.wait(2)