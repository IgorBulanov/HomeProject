'''
Created on 15 мая 2018 г.

@author: Igor
'''
import tkinter as tk
from tkinter import ttk
#import radar.BaseItem as bts
import radar.ItemSet as iset
import radar.WindowItemTypeSelector as wits
from random import randint

# RAISED
# SUNKEN
# GROOVE
# RIDGE

class WindowItemSet(iset.ItemSet):
    def __init__(self, parent4items, parent4buttons, parent4drawFrame, *args, **kw):
        self.parent4items = parent4items
        self.parent4buttons = parent4buttons
        self.parent4drawFrame = parent4drawFrame
        super(WindowItemSet, self).__init__(*args, **kw)
        f2 = self.parent4buttons
        b_reset = ttk.Button(f2, text = "Reset", command=self.reset)
        b_arun = ttk.Button(f2, text = "Auto Run", command=self.autoRun)
        b_add = ttk.Button(f2, text = "Add", command=lambda p=self.parent4items : self.addItem(p) )
        b_reset.pack(side=tk.LEFT, expand=True)
        b_arun.pack(side=tk.LEFT, expand=True)
        b_add.pack(side=tk.LEFT, expand=True)


    def addItem(self, parent):
        wits.WindowItemTypeSelector(parent, self)
    def autoRun(self):
        pass
    def reset(self):
        pass




