import radar.WindowConfig as wc

class WindowConfigFileInput(wc.WindowConfig):
    def __init__(self,
                 parent=None,
                 frameTitle= "File input Configurator",
                 winItemObject=None,
                 itemSet=None,
                 geometry="300x400+400+300",
                 *arg, **kw):
        super(WindowConfigFileInput, self).__init__(*arg, **kw)
