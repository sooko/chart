from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import StringProperty,NumericProperty,ListProperty,BooleanProperty,ObjectProperty,DictProperty
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color,Line,Rotate,Translate,PopMatrix,PushMatrix,Rectangle
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import sp,dp
Builder.load_string("""

<Label_x>:
    

<Label_y>:

<Cagak_x>:
    size_hint:None,1
    width:sp(1)
    canvas:
        Color:
            rgba:1,1,1,.5
        Rectangle:
            size:self.size
            pos:self.pos

<Cagak_y>:
    size_hint:1,None
    height:sp(1)
    canvas:
        Color:
            rgba:1,1,1,.5
        Rectangle:
            size:self.size
            pos:self.pos
<Plot>
<Chart>:
    root_plot:root_plot
    root_labelx:root_labelx
    BoxLayout:
        orientation:"vertical"
        pos_hint:{"center_x":.5,"center_y":.5}
        BoxLayout:
            Button
                size_hint:None,1
                width:dp(30)
            FloatLayout:
                pos_hint:{"center_x":.5,"center_y":.5}
                FloatLayout:
                    pos_hint:{"center_x":.5,"center_y":.5}
                    id:root_plot
                    on_pos:root.change_dimention()
                    on_size:root.change_dimention()
                Plot:
                    pos_hint:{"center_x":.5,"center_y":.5}
        BoxLayout
            size_hint:1,None
            height:dp(30)
            Label
                size_hint:None,1
                width:dp(30)
                text:"0"
            BoxLayout:
                id:root_labelx
                # size_hint:1,1
                # width:self.minimum_width
                canvas.before:
                    PushMatrix
                    Translate:
                        x:-self.width/root.x_major/2
                        y:0
                        z:0
                canvas.after:
                    PopMatrix



""")
class Label_x(Label):
    pass

class Label_y(Label):
    pass

class Plot(Widget):
    pass

class Cagak_x(Widget):
    pass

class Cagak_y(Widget):
    pass
class Chart(FloatLayout):
    x_major=NumericProperty(10)
    y_major=NumericProperty(10)
    x_max=NumericProperty(100)
    y_max=NumericProperty(100)
    x_min=NumericProperty(0)
    y_min=NumericProperty(0)
        

    def __init__(self, **kwargs):
        super(Chart,self).__init__(**kwargs)


    def change_dimention(self,*args):
        self.root_plot.clear_widgets()
        self.root_labelx.clear_widgets()
        for i in range(self.x_major+1):
            self.root_plot.add_widget(Cagak_x(pos=(self.root_plot.x+(i*self.root_plot.width/self.x_major),self.root_plot.y)))
            self.root_labelx.add_widget(Button(width=self.root_labelx.width/self.x_major))

        for i in range(self.y_major):
            self.root_plot.add_widget(Cagak_y(pos=(self.root_plot.x,self.root_plot.y+(i*self.root_plot.height/self.y_major))))





class Graph(App):
    def build(self):
        return Chart()
if __name__=="__main__":
    Graph().run()
