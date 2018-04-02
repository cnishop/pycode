import wx
import turtle
##app=wx.App()
##frame=wx.Frame(parent =None)
##frame.Show()
##app.MainLoop()

##class MyFrame(wx.Frame):
##    pass

class MyApp(wx.App):
    def OnInit(self):
        frame=wx.Frame(parent= None,title='my frame',
                       size=(400,200),
                        pos=(30,100),
                       )
        panel=wx.Panel(frame,-1)
        self.buttonWJX =wx.Button(panel,-1,"五角星",pos=(10,10),
                                  size =(50,50)
                                  )
        self.Bind(wx.EVT_BUTTON,self.OnButtonWJX,self.buttonWJX)      
        frame.Show()
        return True
    def OnButtonWJX(self,event):
        for i in range(5):
            turtle.forward(150)
            turtle.right(144)


if __name__ == "__main__":
    app =MyApp()
    app.MainLoop()

