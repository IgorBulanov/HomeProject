import tkinter as tk
from tkinter import ttk
import radar.StaticType as st
import radar.WindowBase4Item as wb4i
import radar.WindowFileInputItem as wfii
import radar.WindowFileOutputItem as wfoi
import radar.WindowTestSignalItem as wtsi

class WindowItemTypeSelector(object):
    def __init__(self, parent, itemSet):
        self.parent = parent
        self.itemSet = itemSet
        self.top = tk.Toplevel(parent)
        self.top.title("Item Type Selector")
        self.top.geometry("")   #300x200+400+300
        self.top.focus_force()          ### make modal window ###
        #self.top.grab_set()
        self.top.focus_set()
        self.top.transient(self.parent) ### end of modal window ###
        
        headLabel = tk.Label(self.top, text='Pattern type to cteate item.')
        headLabel.pack(fill=tk.X, side=tk.TOP)
        self.varSelect = tk.IntVar()
        n=1
        for e in st.StaticType.addItemList:
            #command=self.selectItem
            rb = tk.Radiobutton(self.top, text=e, variable=self.varSelect, value=n)
            rb.pack( anchor = tk.W )
            n+=1
        b_cancel = ttk.Button(self.top, text = "Cancel", command=self.cancel)
        b_select = ttk.Button(self.top, text = "Select", command=self.selectItem)
        b_cancel.pack(side=tk.LEFT, anchor=tk.S, padx=5, pady=5, expand=True)
        b_select.pack(side=tk.LEFT, anchor=tk.S, padx=5, pady=5, expand=True)
    
    def cancel(self):
        self.top.destroy()
    
    def selectItem(self):
        #print ( self.varSelect.get() )
        if self.varSelect.get() == 1:   # InputFile
            e=wfii.WindowFileInputItem(parent = self.parent,frameTitle= "File Input Item",itemSet = self.itemSet)
            return
        if self.varSelect.get() == 2:   # OutputFile
            e=wfoi.WindowFileOutputItem(parent = self.parent,frameTitle= "File Output Item",itemSet = self.itemSet)
            return
        if self.varSelect.get() == 3:   # Display
            return
        if self.varSelect.get() == 4:   # Filter1
            return
        if self.varSelect.get() == 5:   # Filter2
            return
        if self.varSelect.get() == 6:   # TestSignal
            e=wtsi.WindowTestSignalItem(parent = self.parent,frameTitle= "Test Signal Creator Item",
                                        itemSet = self.itemSet,geometry="500x400+600+300")
            return
        

