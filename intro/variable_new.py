from manim import *
from PIL import Image
import numpy as np
import urllib.request
from pathlib import Path


class EmojiSVGMobject(SVGMobject):
    def __init__(self, emoji, **kwargs):
        emoji_code = '-'.join(f'{ord(c):x}' for c in emoji)
        emoji_code = emoji_code.upper()  # <-  needed for openmojis
        url = f'https://raw.githubusercontent.com/hfg-gmuend/openmoji/master/color/svg/{emoji_code}.svg'
        path_svg = Path.cwd() / f'{emoji_code}.svg'
        urllib.request.urlretrieve(url, path_svg)
        SVGMobject.__init__(self, str(path_svg), **kwargs)
        path_svg.unlink()  # delete downloaded svg again locally


class Variable(Scene):
    def construct(self):
        # Create objects
        variable = Text('Variable')

        toy = EmojiSVGMobject('🧸').move_to(LEFT*3)
        toy_box = SurroundingRectangle(
            toy, buff=1)
        toy_box_name = Tex(
            "Toys", color=BLUE).next_to(toy_box, UP, buff=0.5)

        # int_str = Tex('Number', r'Word', r'Sentense', font_size=144)
        # int_str.set_color_by_tex('Number', RED)
        # int_str.set_color_by_tex('Word', BLUE)
        # int_str.set_color_by_tex('Sentense', GREEN)

        candy = EmojiSVGMobject('🍬').move_to(RIGHT*3)

        candy_box = SurroundingRectangle(
            candy, buff=1)
        candy_box_name = Tex(
            "Candy", color=BLUE).next_to(candy_box, UP, buff=0.5)
        
        
        veriable_x = Text('x', color=YELLOW).move_to(UP*2)
        memory = Text("Memory", color=BLUE_E).to_edge(UL)
        code = Text("Code", color=BLUE_E).to_edge(UR)

        two = Text("2", color=RED).move_to(UL*2)
        five = Text("5", color=RED)

        code_example = Tex("x", " = ", "2", " + ", "3").move_to(RIGHT*3)
        code_example.set_color_by_tex('x', YELLOW)
        code_example.set_color_by_tex('2', RED)

        square = always_redraw(
            lambda: Square().next_to(veriable_x, DOWN, buff=0.5))

        line = Line(UP*4, DOWN*4)

        # play the objects

        # box num_box
        self.play(Write(variable))
        self.wait(1)
        self.play(variable.animate.to_edge(DL).scale(0.4))

        self.wait(1)
        self.play(Create(VGroup(toy, candy)))
        self.wait(1)

        self.play(Create(VGroup(toy_box, candy_box)))
        self.wait(1)

        self.play(Indicate(VGroup(toy, candy,toy_box, candy_box)))
        self.wait(1)

        self.play(Create(VGroup(toy_box_name, candy_box_name)))
        self.wait(1)

        self.play(FocusOn(toy_box_name), flash_radius=0.7)
        self.wait(1)
        self.play(FocusOn(candy_box_name), flash_radius=0.7)
        self.wait(1)


        self.play(toy_box.animate.set_fill(YELLOW, opacity=0.5), FadeOut(toy))
        self.play(candy_box.animate.set_fill(
            YELLOW, opacity=0.5), FadeOut(candy))
        self.wait(1)

        self.play(toy_box_name.animate.move_to(toy_box.get_center()))
        self.play(candy_box_name.animate.move_to(candy_box.get_center()))

        self.wait(2)
        
        self.play(FadeOut(VGroup(toy_box_name, toy_box), shift=LEFT))
        self.play(FadeOut(VGroup(candy_box_name, candy_box), shift=RIGHT))
        # self.play(Create(num_box))
        # self.play(Rotate(num_box, PI))
        self.wait()
        
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
        self.wait(1)
        self.play(two.animate.move_to(square.get_center()),
                  Write(code_example[1]), FadeOut(curved))
        self.wait()

        brace_ = Brace(code_example[1], direction=UP)
        b1text_ = brace_.get_text("assignmet").scale(0.7).set_color(GREEN)

        self.play(Create(brace_), Write(b1text_,))

        brace_value = Brace(code_example[2], direction=RIGHT)
        b1text_value = brace_value.get_text("value").scale(0.7).set_color(RED)

        self.play(Create(brace_value), Write(b1text_value))

        self.wait(2)

        brace_x = Brace(code_example[0], direction=DOWN)
        b1text_x = brace_x.get_text("Variable name").scale(0.7)

        self.play(Create(brace_x), Write(b1text_x))

        self.play(FadeOut(VGroup(b1text_, brace_), shift=UP))

        self.play(FadeOut(VGroup(b1text_value, brace_value), shift=RIGHT))

        self.play(FadeOut(VGroup(b1text_x, brace_x), shift=DOWN))

        self.wait(2)

        self.play(Write(code_example[3]), Write(code_example[4]))
        self.wait()

        five.move_to(square.get_center())
        self.play(ReplacementTransform(two, five))
        self.wait()


        # number Word sentences
        # self.play(Write(int_str[0]))
        # self.play(ReplacementTransform(int_str[0], int_str[1]))
        # self.play(ReplacementTransform(int_str[1], int_str[2]))
        # self.play(FadeOut(int_str[2]))

        # # box number animation
        # self.play(Write(num_box_name))
        # self.play(FadeIn(num))
        # self.wait()
        # self.play(num.animate.shift(LEFT*5))
        # self.wait()

        # self.play(Create(nam_box))
        # self.play(Rotate(nam_box, PI))
        # self.wait()

        # # box number animation
        # self.play(Write(nam_box_name))
        # self.play(FadeIn(nam))
        # self.wait()
        # self.play(nam.animate.shift(RIGHT*5))
        # self.wait()

        # self.play(Flash(num_box_name, flash_radius=0.7), rate_time=2)
        # self.play(Flash(nam_box_name, flash_radius=1), rate_time=2)
        # FocusOn,Indicate,


class Variable1(Scene):
    def construct(self):
        veriable_x = Text('x', color=YELLOW).move_to(UP*2)
        memory = Text("Memory", color=BLUE_E).to_edge(UL)
        code = Text("Code", color=BLUE_E).to_edge(UR)

        two = Text("2", color=RED).move_to(UL*2)
        five = Text("5", color=RED)

        code_example = Tex("x", " = ", "2", " + ", "3").move_to(RIGHT*3)
        code_example.set_color_by_tex('x', YELLOW)
        code_example.set_color_by_tex('2', RED)

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
        self.wait(1)
        self.play(two.animate.move_to(square.get_center()),
                  Write(code_example[1]), FadeOut(curved))
        self.wait()

        brace_ = Brace(code_example[1], direction=UP)
        b1text_ = brace_.get_text("assignmet").scale(0.7).set_color(GREEN)

        self.play(Create(brace_), Write(b1text_,))

        brace_value = Brace(code_example[2], direction=RIGHT)
        b1text_value = brace_value.get_text("value").scale(0.7).set_color(RED)

        self.play(Create(brace_value), Write(b1text_value))

        self.wait(2)

        brace_x = Brace(code_example[0], direction=DOWN)
        b1text_x = brace_x.get_text("Variable name").scale(0.7)

        self.play(Create(brace_x), Write(b1text_x))

        self.play(FadeOut(VGroup(b1text_, brace_), shift=UP))

        self.play(FadeOut(VGroup(b1text_value, brace_value), shift=RIGHT))

        self.play(FadeOut(VGroup(b1text_x, brace_x), shift=DOWN))

        self.wait(2)

        self.play(Write(code_example[3]), Write(code_example[4]))
        self.wait()

        five.move_to(square.get_center())
        self.play(ReplacementTransform(two, five))
        self.wait()
