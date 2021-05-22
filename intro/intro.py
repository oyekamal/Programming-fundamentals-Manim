from manim import *

class Intro(Scene):
    def construct(self):
        ok = Text("OK",  t2c={'O':YELLOW}).scale(2)
        oykamal = Text("oykamal", t2c={'oy':YELLOW}).scale(2)
        lets = Text("lets start")
        
        
        message = TextMobject(r"I'm going to teach you the basic concept of ", r"Programming.")
        message[1].set_color(YELLOW)
        message1 = TextMobject(r"Which are use in lot of ", r"Programming ", r"language.").scale(0.5)
        message1[1].set_color(YELLOW)
        example = Text("For Example.", color=RED)
        
        list_of_content = TextMobject(
        '$\\bullet$ Display Text on screen \\\\',
        '$\\bullet$ Variable \\\\',
        '$\\bullet$ Loop/Nested Loop \\\\',
        '$\\bullet$ Array \\\\',
        '$\\bullet$ Condition \\\\',
        '$\\bullet$ Function \\\\',
        '$\\bullet$ Class \\\\',
        )
        
        message.next_to(message1,UP)        
        ok.next_to(lets, UP)
        
        self.wait(2)
        # self.play(Write(ok))
        self.play(Write(oykamal),run_time=5)
        self.wait(2)
        self.play(ReplacementTransform(oykamal,ok))
        self.play(Write(lets))
        self.play(FadeOut(ok),FadeOut(lets))
        self.wait(2)
        self.play(Write(message),Write(message1))
        self.wait(3)
        self.play(FadeOut(message),FadeOut(message1))
        self.play(Write(example))
        self.play(example.animate.scale(0.4).to_edge(UP).to_edge(LEFT))
        self.wait(1)
        self.play(Write(list_of_content))
        self.wait(2)
        self.play(list_of_content[0].set_color(RED).animate.to_edge(UP),FadeOut(list_of_content[1:]))
        self.wait(2)