# -*- coding: utf-8 -*-
import wx
app=wx.App()#初始化应用程序
win=wx.Frame(None,title="Simple Editor")
win.Show()#创建一个Frame（窗体），并显示出来
loadButton=wx.Button(win,label='Open',pos=(225,5),size=(80,25))
saveButton=wx.Button(win,label='save',pos=(315,5),size=(80,25))
filename=wx.TextCtrl(win,pos=(5,5),size=(210,25))
content=wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)#wx.TE_MULTILINE用来获取多行文本区（默认有垂直滚动条）以及wx.HSCROLL获取水平滚动条


#btn=wx.Button(win)

app.MainLoop()#应用程序进入消息循环
