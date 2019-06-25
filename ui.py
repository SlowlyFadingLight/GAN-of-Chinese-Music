import wx
import wx.xrc
import pygame
import time
from GAN import *

gan = GAN(rows = 100)

class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY,title = wx.EmptyString,pos = wx.DefaultPosition, size = wx.Size( 623,396 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"欢迎使用民乐生成系统", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"请选择一个乐器", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        m_choice1Choices = [ u"古筝", u"二胡" ]
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer1.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"点击生成民乐", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"点击播放音乐", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.get_minyue)
        self.m_button2.Bind( wx.EVT_BUTTON, self.play_music )
	#self.m_button2.Bind
    def __del__( self ):
        pass
    def get_minyue( self, event ):
        if (self.m_choice1.GetStringSelection() == u'古筝'):
            gan.generate(inst = 'guzhen',name = 'minyue')
        if(self.m_choice1.GetStringSelection() == u'二胡'):
            gan.generate(inst = 'erhu',name = 'minyue')
        event.Skip()

    def play_music( self, event ):
        pygame.mixer.init()
        track = pygame.mixer.music.load('minyue.mid')
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.mixer.music.stop()
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    main_win = MyFrame1(None)
    
    main_win.Show()
    app.MainLoop()
