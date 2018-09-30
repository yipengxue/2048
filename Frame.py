#! /usr/bin/python
# Filename:Frame.py
# coding:utf-8

import wx

class Example(wx.Frame):
    def __init__(self, title):
        super(Example,self).__init__(None, title=title, size=(500, 500))
        self.Centre()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    Example('test')
    app.MainLoop()
    
