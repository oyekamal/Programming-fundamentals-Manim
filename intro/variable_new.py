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

        int_str = Tex('Number', r'Word', r'Sentense', font_size=144)
        int_str.set_color_by_tex('Number', RED)
        int_str.set_color_by_tex('Word', BLUE)
        int_str.set_color_by_tex('Sentense', GREEN)

        nam = Text('Kamal')
        nam_box = always_redraw(lambda: SurroundingRectangle(
            nam, buff=1))
        nam_box_name = always_redraw(lambda: Tex(
            "name", color=GREEN).next_to(nam_box, UP, buff=0.5))

        # play the objects

        # box num_box
        self.play(Write(variable))
        self.wait(1)
        self.play(variable.animate.to_edge(UL).scale(0.4))

        self.play(Create(num_box))
        self.play(Rotate(num_box, PI))
        self.wait()

        # number Word sentences
        self.play(Write(int_str[0]))
        self.play(ReplacementTransform(int_str[0], int_str[1]))
        self.play(ReplacementTransform(int_str[1], int_str[2]))
        self.play(FadeOut(int_str[2]))

        # box number animation
        self.play(Write(num_box_name))
        self.play(FadeIn(num))
        self.wait()
        self.play(num.animate.shift(LEFT*5))
        self.wait()

        self.play(Create(nam_box))
        self.play(Rotate(nam_box, PI))
        self.wait()

        # box number animation
        self.play(Write(nam_box_name))
        self.play(FadeIn(nam))
        self.wait()
        self.play(nam.animate.shift(RIGHT*5))
        self.wait()

        self.play(Flash(num_box_name, flash_radius=0.7), rate_time=2)
        self.play(Flash(nam_box_name, flash_radius=1), rate_time=2)


class Variable1(Scene):
    def construct(self):
        veriable_x = Text('x', color=YELLOW).move_to(UP*2)
        memory = Text("Memory", color=BLUE_E).to_edge(UL)
        code = Text("Code", color=BLUE_E).to_edge(UR)

        two = Text("2", color=RED).move_to(UL*2)
        five = Text("5", color=RED)

        code_example = Tex("x", " = ", "2", " + ", "3").move_to(RIGHT*3)

        square = always_redraw(
            lambda: Square().next_to(veriable_x, DOWN, buff=0.5))

        line = Line(UP*4, DOWN*4)

        # animation
        self.play(Create(veriable_x), Create(square))
        self.play(veriable_x.animate.shift(UP*1))
        self.wait()
        # self.play()
        self.play(Rotate(square, PI))
        self.play(veriable_x.animate.shift(DOWN*1).shift(LEFT*5))
        # self.play(veriable_x.animate.move_to(DOWN).move_to(LEFT*5))

        curved = always_redraw(lambda: CurvedArrow(
            two.get_bottom(), square.get_center(), color=BLUE_E))

        self.play(Create(line))
        self.play(Create(memory), Create(code), Write(code_example[0]))
        self.wait()
        self.play(Write(two),  Write(code_example[2]))
        self.wait()
        self.play(Create(curved))
