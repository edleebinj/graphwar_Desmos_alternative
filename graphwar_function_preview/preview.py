import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import numpy as np
from sympy import *
from win32clipboard import OpenClipboard,GetClipboardData,CloseClipboard
from minwinpy import minwinpy
class InteractiveGraph:
    def __init__(self, samplenum = 100):
        self.samplenum = samplenum
        self.func = "x"
        self.x_min = -25
        self.x_max = 25
        self.y_min = -14.6
        self.y_max = 14.6
        self.shooter_coord=(0,0)
        self.draw_gui()
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        plt.show()
    def draw_gui(self):#Add GUIs to figure
        self.fig = plt.figure()
        self.ax = self.fig.subplots()
        plt.subplots_adjust(left = 0.15, bottom = 0.25)
        self.ax.set_title("Graphwar function preview")
        self.ax.set_xlabel("x axis")
        self.ax.set_ylabel("y axis")
        x, y = self.get_coords()
        self.plot, = self.ax.plot(x, y, color="blue", marker="o",ms=0)
        axesFunctionText = plt.axes([0.1, 0.01, 0.55, 0.05])
        self.textFunction = TextBox(axesFunctionText, label="y =", initial=self.func)
        self.textFunction.on_submit(self.get_func)
        self.pastebtn = Button(plt.axes([0.81, 0.01, 0.1, 0.05]), 'paste', color = "white")
        self.pastebtn.on_clicked(self.paste_func)
        self.update_background_btn = Button(plt.axes([0.70, 0.01, 0.1, 0.05]), 'update', color = "white")
        self.update_background_btn.on_clicked(self.update_background)
        self.ax.set_ylim([self.y_min,self.y_max])
    def get_coords(self):#Get coords to draw
        xs = np.linspace(self.x_min, self.x_max, self.samplenum)
        x= symbols('x')
        ans= sympify(self.func)
        ys = [float(ans.subs(x,i)) for i in xs]
        return xs, ys
    def get_func(self, text):#Update function
        if self.func != text:
            self.func = text#need traslations
            self.draw()
    def paste_func(self,event):#paste function from clipboard
        OpenClipboard()
        data = GetClipboardData()
        CloseClipboard()
        if self.func != data:
            self.func = data
            self.textFunction.set_val(data)
            self.draw()
    def draw(self):#draw the plot
        x, y = self.get_coords()

        x_x= symbols('x')
        ans= sympify(self.func)
        y_translation_by_player_coord = float(ans.subs(x_x,self.shooter_coord[0]))#f(a)

        y_numpar = np.array(y)
        self.plot.set_xdata(x)
        y_input = y_numpar-y_translation_by_player_coord+self.shooter_coord[1]#y-f(a)+b
        self.plot.set_ydata(y_input.tolist())
        plt.show()
    def update_background(self,event):
        WindowsName="Graphwar"
        yourWindows= minwinpy(WindowsName)
        yourWindows.Screenshot("temp",(22,45),(772,452))
        img = plt.imread("temp.png",format ='jpeg')
        self.ax.imshow(img,extent=[-25,25,-14.6,14.6])
        self.draw()
    def onclick(self,event):
        ix, iy = event.xdata, event.ydata
        coords=(ix, iy)
        self.shooter_coord = coords
        self.draw()
if __name__ == "__main__":
  g = InteractiveGraph()