#coding:utf-8
import ipywidgets as wids

class Palette(object):
    def __init__(self, col:int=None, row:int=None):
        self.col = col
        self.row = row
        self.widgets = [[None for row_i in range(row)] for col_i in range(col)]
        self.widget = None

    def show(self):
        return self.widget

    def add_widget(self, col=None, row=None, widget=None):
        self.widgets[col][row] = widget

    def build(self):
        vboxs = list()
        for col_i, widgets in enumerate(self.widgets):
            col_widgets = [widget for widget in widgets]
            vboxs.append(wids.VBox(col_widgets))
        self.widget = wids.HBox(vboxs)