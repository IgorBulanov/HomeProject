'''
Created on 1 мая 2018 г.

@author: Igor
'''
import tkinter as tk
from tkinter import ttk
import radar.MainMenu as mm
import radar.ScrolledFrame as sf
from tkinter import messagebox, filedialog
import radar.WindowItemSet as wis
import radar.Config as cfg

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(cfg.Config.winTitle)
        self.minsize(cfg.Config.minSizeWidth, cfg.Config.minSizeHeight)
        self.geometry("{}x{}+{}+{}".format(self.winfo_screenwidth()-10, self.winfo_screenheight()-100,0 ,0))
        mmenu=mm.MainMenu(self)
        self.config(menu=mmenu.menubar)
        self.mainTabs = MainTabsPane(self)
        self.itself = self
    
    def getItself(self):
        return self.itself

    def run(self):
        self.mainloop()

class MainTabsPane(object):
    def __init__(self, root):
        self.panes = {}    #Tab name => pane
        self.nb = ttk.Notebook(root)
        self.nb.pack(fill=tk.BOTH, expand=1)
        self.add_tabs(nameTabs="MainTab")
        self.add_tabs(nameTabs="Project-1")
        self.add_tabs(nameTabs="Project-2")
        self.add_tabs(nameTabs="Project-3")

    def add_tabs(self, nameTabs='MainTab'):
        if self.panes.get(nameTabs) is None:
            self.panes[nameTabs] = ttk.Frame(self.nb)
            self.panes[nameTabs].pack(fill=tk.BOTH, expand=True)
            self.nb.add(self.panes.get(nameTabs), text=nameTabs)
            self.interior = MainInteriorPane(self.panes[nameTabs]);
        else:
            tk.messagebox.showwarning("Redefinition", nameTabs+" have existed.\n"+
                                      "Redefine, please.")

class MainInteriorPane(object):
    def __init__(self, root):
        self.mainPane = tk.PanedWindow(root, orient=tk.HORIZONTAL,
                                       relief="groove", borderwidth=2)
        self.leftPane = tk.PanedWindow(root, orient=tk.VERTICAL,
                                       relief="groove", borderwidth=2,
                                       width=400)
        self.rightPane = tk.PanedWindow(root, orient=tk.VERTICAL,
                                        relief="groove", borderwidth=2)
        self.mainPane.add(self.leftPane)
        self.mainPane.add(self.rightPane)
        self.mainPane.pack(fill=tk.BOTH, expand=True)

        self.interiorLeftPane()     #inside created self.sframe, self.b_frame ;
        self.interiorRightPane()    #inside created self.rframe ;
        #self.leftPaneUnitSet = wis.WindowItemSet(sframe.interior, self.leftPane)
        self.leftPaneUnitSet = wis.WindowItemSet(self.sframe.interior, self.b_frame, self.rframe)
        
    def interiorLeftPane(self):
        up_frame = tk.Frame(self.leftPane, relief="groove", borderwidth=2)
        up_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True) #
        self.sframe = sf.ScrolledFrame(up_frame)
        self.sframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True) #
        self.b_frame = tk.Frame(self.leftPane, relief="groove", borderwidth=2)
        self.b_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=False)

    def interiorRightPane(self):
        # for debug, later must be delete;
        rf1 = tk.Frame(self.rightPane, relief="groove", borderwidth=2)
        rf1.pack(fill=tk.BOTH, expand=1)
        self.rframe = sf.ScrolledFrame(rf1)
        self.rframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

