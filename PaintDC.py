#! /usr/bin/python
# Filename:PaintDC.py
#coding: utf-8

import wx

class Example(wx.Frame):
    def __init__(self, title):
        super(Example, self).__init__(None, title=title, size=(500,500))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Centre()
        self.Show()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.DrawLine(50, 60 ,190 ,60)
        dc.DrawLine(190, 60, 190, 80)
        dc.DrawLine(190, 80, 50, 100)
        dc.DrawLine(50, 100, 50, 60)


if __name__ == '__main__':
    app = wx.App()
    Example('line')
    app.MainLoop()
