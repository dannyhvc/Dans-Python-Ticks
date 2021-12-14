import wx


def main():
    app = wx.App(clearSigInt=True)
    frame = wx.Frame(parent=None,
                     id=wx.ID_ANY,
                     title="Hello World",
                     pos=(100,100))
    panel = wx.Panel(parent=frame, id=wx.ID_ANY)
    welcome = wx.StaticText(parent=panel, label="Hello World", pos=(20,20))

    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
