from wx import Frame, Panel, App, StaticText, TopLevelWindow, ID_ANY


class MyApp(App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.init_frame()

    def init_frame(self):
        frame = Frame(None, title="Hello World", pos=(100, 100))
        frame.Show()


class MyFrame(Frame):
    def __init__(
        self,
        parent: TopLevelWindow,
        title: str,
        pos: tuple[int, int],
    ) -> None:
        super().__init__(parent=parent, title=title, pos=pos)
        self.on_init()

    def on_init(self):
        panel = MyPanel(parent=self)


class MyPanel(Panel):
    def __init__(self, parent: TopLevelWindow):
        super().__init__(parent=parent)
        StaticText(parent=self, id=ID_ANY, label="Hello World!", pos=(20, 20))


def main():
    app = MyApp()
    app.MainLoop()


if __name__ == '__main__':
    main()
