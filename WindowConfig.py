import tkinter as tk
from tkinter import ttk
import radar.StaticType as st
import radar.ScrolledFrame as sf
import radar.Config as cfg


class WindowConfig(cfg.Config):
    def __init__(self,
                 parent=None,
                 frameTitle= "Item Configurator",
                 winItemObject=None,
                 itemSet=None,
                 geometry="300x400+400+300",
                 *arg, **kw):
        self.parent = parent
        self.frameTitle=frameTitle
        self.winItemObject=winItemObject
        self.itemSet=itemSet
        self.geometry=geometry
        super(WindowConfig, self).__init__(*arg, **kw)
        
        self.top = tk.Toplevel(self.parent)
        self.top.title(self.frameTitle)
        self.top.geometry(self.geometry)
        self.top.focus_force()          ### make modal window ###
        #self.top.grab_set()
        self.top.focus_set()
        self.top.transient(self.parent) ### end of modal window ###

#        up_frame = ttk.Frame(self.top, relief="groove", borderwidth=2)
#        up_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        #self.sframe = sf.ScrolledFrame(up_frame)
        #self.sframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        b_frame = tk.Frame(self.top, relief="groove", borderwidth=2)
        #b_frame = tk.Frame(self.sframe.interior, relief="groove", borderwidth=2)
        b_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=False)

        b_cancel = ttk.Button(b_frame, text = "Cancel", command=self.onCancel)
        b_select = ttk.Button(b_frame, text = "Apply", command=self.onApply)
        b_cancel.pack(side=tk.LEFT, padx=5, pady=5, expand=True)
        b_select.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

    def onCancel(self):
        self.top.destroy()
        
    def onApply(self):
        pass
    
    def loadFields(self):
        pass
