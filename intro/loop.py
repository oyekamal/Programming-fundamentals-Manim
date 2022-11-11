from manim import *




class Loop(Scene):
    def construct(self):
        loop = Tex('Loop ')
        
        
        self.play(Write(loop))
        self.wait()
        self.play(loop.animate.to_edge(UL).scale(0.6))
        
        self.wait()
        
        p = RegularPolygon(20, color=DARK_GRAY, stroke_width=6).scale(3)
        lbl = VMobject()
        self.add(p, lbl)
        p = p.copy().set_color(BLUE)
        for time_width in [0.2, 0.5, 1, 2]:
            lbl.become(Tex(r"\texttt{time\_width={{%.1f}}}"%time_width))
            self.play(ShowPassingFlash(
                p.copy().set_color(BLUE),
                run_time=2,
                time_width=time_width
            ))