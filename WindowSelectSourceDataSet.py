import tkinter as tk
from tkinter import ttk
import radar.StaticType as st
import radar.ScrolledFrame as sf

class WindowSelectSourceDataSet(object):
    def __init__(self,
                 winItemObject=None,
                 parent=None,
                 itemSet=None,
                 *args, **kw):
        self.winItemObject = winItemObject
        self.parent = parent
        self.itemSet = itemSet
        super(WindowSelectSourceDataSet, self).__init__(*args, **kw)
        
        self.sourceNameSet = []
        self.createSourceNameSet()
        self.top = tk.Toplevel(parent)
        self.top.title("Source Data Set Selector")
        self.top.geometry("300x400+400+300")
        self.top.focus_force()          ### make modal window ###
        #self.top.grab_set()
        self.top.focus_set()
        self.top.transient(self.parent) ### end of modal window ###

        up_frame = tk.Frame(self.top, relief="groove", borderwidth=2)
        up_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        sframe = sf.ScrolledFrame(up_frame)
        sframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        b_frame = tk.Frame(self.top, relief="groove", borderwidth=2)
        b_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=False)
        
        headLabel = tk.Label(sframe.interior, text='Select data source for this item.')
        headLabel.pack(fill=tk.X, side=tk.TOP)
        self.varSelectSourceName = tk.IntVar()
        n=1
        for e in self.sourceNameSet:
            rb = tk.Radiobutton(sframe.interior, text=e, variable=self.varSelectSourceName, value=n)
            rb.pack( side=tk.TOP, anchor = tk.W )
            n+=1

        b_cancel = ttk.Button(b_frame, text = "Cancel", command=self.onCancel)
        b_select = ttk.Button(b_frame, text = "Select", command=self.onSelect)
        b_cancel.pack(side=tk.LEFT, padx=5, pady=5, expand=True)
        b_select.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

    def onCancel(self):
        self.top.destroy()
        
    def onSelect(self):   #self.varSelectSourceName
        self.winItemObject.varSourceName.set(self.sourceNameSet[self.varSelectSourceName.get()-1])
        self.winItemObject.messageOut(st.StaticType.msg_not_saved)
        self.top.destroy()
        
    def createSourceNameSet(self):
        self.sourceNameSet.append(st.StaticType.UnkownName)
        for e in self.itemSet.unitSet:
            self.sourceNameSet.append(e.dataSetName)

