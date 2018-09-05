import tkinter as tk
from tkinter import ttk
import radar.WindowBase4Item as wb4i

class WindowFileInputItem(wb4i.WindowBase4Item):
    def __init__(self,
                 parent = None,
                 frameTitle= "File Input Item",
                 itemSet = None,
                 *args, **kw):
        #self.parent = parent
        #self.itemSet = itemSet
        #self.frameTitle = frameTitle
        super(WindowFileInputItem, self).__init__(parent=parent,
                                                  frameTitle=frameTitle,
                                                  itemSet = itemSet,
                                                  *args, **kw)
        #self.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        #self.config(relief=tk.GROOVE)
    
    





