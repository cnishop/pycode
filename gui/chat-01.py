import wx
import time
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"guo's chat",size=(520,450))
        panel = wx.Panel(self)
        labelAll=wx.StaticText(panel,-1,"All Contents",pos=(180,0))
        self.textAll= wx.TextCtrl(panel,-1,
                                  size=(480,200),
                                  pos=(10,25),
                                  style=wx.TE_MULTILINE|wx.TE_READONLY)

        lableIn=wx.StaticText(panel,-1,"I Say",pos=(180,230))
        self.textIn = wx.TextCtrl(panel,-1,
                                  size=(480,100),
                                  pos=(10,255),
                                  style=wx.TE_MULTILINE)
        
        self.btnSent= wx.Button(panel,-1,"Sent",size = (75,25),pos=(180,360))
        self.btnClear = wx.Button(panel,-1,"Clear",size =(75,25) ,pos=(260,360))
        self.Bind(wx.EVT_BUTTON,self.OnButtonSent,self.btnSent)
        self.Bind(wx.EVT_BUTTON,self.OnButtonClear,self.btnClear)
        
    def OnButtonSent(self,event):
        userinput= self.textIn.GetValue()
        self.textIn.Clear()
        now = time.ctime()
        inmsg = "You (%s): \n%s \n" % (now,userinput)
        self.textAll.AppendText(inmsg)
        #self.textAll.SetValue(userinput)
        
        
    def OnButtonClear(self,event):
        pass

app=wx.App()
frame =MyFrame()
frame.Show()
app.MainLoop()
