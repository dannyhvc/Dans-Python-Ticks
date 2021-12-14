from wx import (App, Frame, TextCtrl, TE_MULTILINE)


class MyFrame(Frame):
    def __init__(self, parent, title):
        Frame.__init__(self, parent, title=title, size=(300, 200))
        self.control = TextCtrl(self, style=TE_MULTILINE)
        self.Show()


def main():
    app = App(False)
    frame = MyFrame(None, "Sample editor")
    app.MainLoop()


if __name__ == "__main__":
    main()
