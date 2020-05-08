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
<Mayor_x>:
    size_hint:None,1
    width:sp(1)
    canvas:
        Color:
            rgba:1,1,1,.6
        Rectangle:
            size:self.size
            pos:self.pos
<Mayor_y>:
    size_hint:1,None
    height:sp(1)
    canvas:
        Color:
            rgba:1,1,1,.6
        Rectangle:
            size:self.size
            pos:self.pos
<Label_x>:
<Label_y>:
    canvas.before:
        PushMatrix
        Rotate:
            angle:45
            origin:self.center
    canvas.after:
        PopMatrix
<Chart>:
    pos_hint:{"center_x":.5,"center_y":.5}
    BoxLayout
        pos_hint:{"center_x":.5,"center_y":.5}
        BoxLayout:
            orientation:"vertical"
            size_hint:None,None
            width:dp(30)
            font_size:self.width
            height:dp(self.parent.height)-dp(30)
            pos_hint:{"center_x":.5,"top":1}
            id:root_plot_label_y
            canvas.before:
                PushMatrix
                Translate:
                    x:0
                    y:self.height/root.major_y/2
                    z:0
            canvas.after:
                PopMatrix
            # we can add label y here
        BoxLayout
            pos_hint:{"center_x":.5,"center_y":.5}
            orientation:"vertical"
            FloatLayout:
                pos_hint:{"center_x":.5,"center_y":.5}
                FloatLayout
                    id:root_plot
                    size_hint:1,1
                    pos_hint:{"center_x":.5,"center_y":.5}
                    # on_size:root.change_size()
                    # on_pos:root.change_size()
                Plot:
                    size_hint:1,1
                    pos_hint:{"center_x":.5,"center_y":.5}
                    id:plt
            BoxLayout
                size_hint:1,None
                height:dp(30)
                pos_hint:{"center_x":.5,"center_y":.5}
                id:root_plot_label_x
                font_size:self.height/2
                canvas.before:
                    PushMatrix
                    Translate:
                        x:self.width/root.major_x/2
                        y:0
                        z:0
                canvas.after:
                    PopMatrix
                Label:
                    text:"{} s/div".format(root.max_x/root.major_x/root.times*root.speed)

""")

class Plot(Widget):
    red         =ObjectProperty(None)
    yellow      =ObjectProperty(None)
    blue        =ObjectProperty(None)
    pink        =ObjectProperty(None)
    orange      =ObjectProperty(None)
    grey        =ObjectProperty(None)
    white       =ObjectProperty(None)
    purple      =ObjectProperty(None)
    aqua        =ObjectProperty(None)
    navy        =ObjectProperty(None)
    coral       =ObjectProperty(None)
    maroon      =ObjectProperty(None)
    teal        =ObjectProperty(None)
    violet      =ObjectProperty(None)
    amber       =ObjectProperty(None)
    cagak       =ObjectProperty(None)
    tebal       =NumericProperty(1.5)
    max_xx      =NumericProperty(100)
    max_yy      =NumericProperty(100)
    min_xx      =NumericProperty(0)
    min_yy      =NumericProperty(0)
    major_xx    =ObjectProperty(None)
    major_yy    =ObjectProperty(None)    
    jal=[50,50,60,60]
    clr=DictProperty({})
    def __init__(self, **kwargs):
        super(Plot,self).__init__(**kwargs)
        with self.canvas.before:
            self.pushmatrix=PushMatrix()
            self.translate=Translate(x=0,y=0,z=0)
            self.r      =Color(rgba=(1,0,0,1))
            self.clr["red"]    =Line(points=[],width=self.tebal)
            self.g      =Color(rgba=(0,1,0,1))
            self.clr["green"]  =Line(points=[],width=self.tebal)
            self.b      =Color(rgba=(0,0,1,1))
            self.clr["blue"]   =Line(points=[],width=self.tebal)
            self.yel    =Color(rgba=(1,1,0,1))
            self.clr["yellow"] =Line(points=[],width=self.tebal)
            self.m      =Color(rgba=(.5,0,0,1))
            self.clr["maroon"] =Line(points=[],width=self.tebal)
            self.pur    =Color(rgba=(1,0,1,1))
            self.clr["purple"] =Line(points=[],width=self.tebal)
            self.p      =Color(rgba=(1,.4,.7,1))
            self.clr["pink"]   =Line(points=[],width=self.tebal)
            self.a      =Color(rgba=(0,1,1,1))
            self.clr["aqua"]   =Line(points=[],width=self.tebal)
            self.na     =Color(rgba=(0,0,.5,1))
            self.clr["navy"]   =Line(points=[],width=self.tebal)
            self.tea    =Color(rgba=(0,.5,.5,1))
            self.clr["teal"]   =Line(points=[],width=self.tebal)
            self.vio    =Color(rgba=(1,.5,1,1))
            self.clr["violet"] =Line(points=[],width=self.tebal)
            self.amb    =Color(rgba=(1,.5,.2,1))
            self.clr["amber"]  =Line(points=[],width=self.tebal)
            self.gr     =Color(rgba=(103/255, 128/255, 159/255, 1))
            self.clr["grey"]   =Line(points=[],width=self.tebal)
            self.putih  =Color(rgba=(1,1,1,1))
            self.clr["white"]  =Line(points=[],width=self.tebal)
        with self.canvas.after:
            self.popmatrix=PopMatrix()
            self.cag        =Color(rgba=(1,1,1,1))          
            self.cagak      =Line(points=[],width=sp(1.5))
    def on_size(self,*args):
        self.cagak.points=[self.x,self.y,self.x,self.height+self.y,
                           self.x,self.y,self.width+self.x,self.y]
    def on_pos(self,*args):
        self.cagak.points=[self.x,self.y,self.x,self.height+self.y,
                           self.x,self.y,self.width+self.x,self.y]
    def set_configure(self,max_xx,max_yy,tt):
        pass
    def draw_Plot(self,xx,yy,times):
        pass
class Label_x(Label):
    pass
class Label_y(Label):
    pass
class Mayor_x(Widget):
    pass
class Mayor_y(Widget):
    pass
class Black(Widget):
    def __init__(self, **kwargs):
        super(Black,self).__init__(**kwargs)
class Chart(FloatLayout):
    rp=ObjectProperty(None)
    plt=ObjectProperty(None)
    rpl=ObjectProperty(None)
    rply=ObjectProperty(None)
    count=0
    realtime=BooleanProperty(True)
    times=NumericProperty(2)
    speed=NumericProperty(.5)

    major_x=NumericProperty(10)
    major_y=NumericProperty(10)
    max_x  =NumericProperty(100)
    max_y  =NumericProperty(100)
    min_y=NumericProperty(0)
    min_x=NumericProperty(0)
    line=DictProperty({"red":[],
                       "green":[],
                       "blue":[],
                       "yellow":[],
                       "maroon":[],
                       "purple":[],         
                       "pink":[],
                       "aqua":[],
                       "navy":[],
                       "teal":[],
                       "violet":[],
                       "amber":[],
                       "grey":[],
                       "white":[],
                                })
    def __init__(self, **kwargs):
        super(Chart,self).__init__(**kwargs)
        self.init()
    def init(self):
        self.data_ready=None
        Clock.unschedule(self.delay)
        Clock.schedule_once(self.delay,.5)
        # if self.realtime:
        #     Clock.schedule_interval(self.timer,self.speed)
    def delay(self,dt):
        self.data_ready=1
        self.plt=self.ids["plt"]
        self.rplx=self.ids["root_plot_label_x"]
        self.rply=self.ids["root_plot_label_y"]
        if self.realtime:
            Clock.unschedule(self.timer,self.speed)
            Clock.schedule_interval(self.timer,self.speed)
        self.a=Mayor_x
        self.b=Mayor_y
        self.rp=self.ids["root_plot"]
        self.rp.clear_widgets()
        self.rply.clear_widgets()
        self.count=0
        if not self.realtime:
            self.rplx.clear_widgets()
        for i in range(self.major_x):
            self.rp.add_widget(self.a(pos=(self.rp.width/self.major_x*i+self.rp.x , self.rp.y)))
            if not self.realtime:
                self.rplx.add_widget(Label_x(text=str(self.major_x+(i*self.major_x))))
        for i in range(self.major_y):
            self.rp.add_widget(self.b(pos=(self.rp.x , self.rp.height/self.major_y*i+self.rp.y)))
            self.rply.add_widget(Label_y(text="{:.1f}".format(self.max_y- (i*(self.max_y-self.min_y)/self.major_y))))
        for i in self.line:
            self.line[i].clear()
    def timer(self,dt):
        if self.realtime:
            self.count+=self.times
            self.draw_line(xx=self.count,yy=10,clr="blue")
            if self.count>self.max_x:
                self.plt.translate.x=self.plt.width-self.plt.width/self.max_x*self.count
    def draw_line(self,clr="white",xx=0,yy=0):
        if self.realtime:
            a=[self.plt.x+(self.count*self.plt.width/self.max_x),self.plt.y+(yy*self.plt.height/self.max_y)   ]
            self.line[clr].append(a)
            self.plt.clr[clr].points=self.line[clr]
            if self.count > self.max_x:
                self.line[clr].remove(self.line[clr][0])
        else:
            a=[self.plt.x+(xx*self.plt.width/self.max_x),self.plt.y+(yy*self.plt.height/self.max_y)]
            self.line[clr].append(a)
            self.plt.clr[clr].points=self.line[clr]
class Graph(App):
    def build(self):
        return Chart()
if __name__=="__main__":
    Graph().run()
