from kivy.app import App
from kivy.uix.stencilview import StencilView
from kivy.graphics import Line, Color
import random

class DrawingPad(StencilView):
    def __init__(self, **kwargs):
        super(DrawingPad, self).__init__(**kwargs)
        self.stroke_width = 2
        self.current_color = (1, 1, 1)

    def increase_stroke_width(self, instance):
        self.stroke_width += 1

    def decrease_stroke_width(self, instance):
        if self.stroke_width > 1:
            self.stroke_width -= 1

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(*self.current_color)
                Line(points=(touch.x, touch.y), width=self.stroke_width)
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.stroke_width)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos) and 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]

    def clear_canvas(self, instance):
        self.canvas.clear()
        self.stroke_width = 2
        self.current_color = (1, 1, 1)

    def change_color(self, instance):
        self.current_color = (random.random(), random.random(), random.random())

class DigitalSketchPadApp(App):
    pass

if __name__ == '__main__':
    DigitalSketchPadApp().run()
