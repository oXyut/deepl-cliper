import pyperclip as pc
import wx

# ゆくゆくはAppクラスを作ってそこに入れる
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            id=-1,
            title='wxPython',
            size=(400, 400),
        )
        self.Show()

# 本体
def clipper():
    clip = pc.waitForNewPaste()
    modified = clip.replace("\r\n", "").replace("\n", "")
    pc.copy(modified)
    print(modified)

if __name__ == '__main__':
    # app = wx.App()
    # frame = MyFrame()
    # app.SetTopWindow(frame) # 省略可能
    # app.MainLoop()
    while True:
        clipper()