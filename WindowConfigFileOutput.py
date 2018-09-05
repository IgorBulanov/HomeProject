import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import radar.WindowConfig as wc
import radar.StaticType as st

class WindowConfigFileOutput(wc.WindowConfig):
    def __init__(self,
                 parent=None,
                 frameTitle= "File output Configurator",
                 winItemObject=None,
                 itemSet=None,
                 *arg, **kw):
        self.parent=parent
        self.frameTitle=frameTitle
        self.winItemObject=winItemObject
        self.itemSet=itemSet
        super(WindowConfigFileOutput, self).__init__(parent=self.parent,
                                                     frameTitle=self.frameTitle,
                                                     winItemObject=self.winItemObject,
                                                     itemSet=self.itemSet,
                                                     *arg, **kw)
        f1 = ttk.Frame(self.top)
        f1.pack(side=tk.TOP, fill=tk.X, expand=False)
        fileName_label=ttk.Label(f1, text= "Output File Name: ")
        fileName_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.varFileName=tk.StringVar()
        self.fileName_entry = ttk.Entry(f1, textvariable=self.varFileName)
        self.fileName_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2, pady=2)
        buttonFile = ttk.Button(f1, text = "File", command=self.onFile)
        buttonFile.pack(side=tk.LEFT, padx=5, pady=5, expand=False)

    def onFile(self):
        self.varFileName.set(fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                     ("DATA files", "*.dat;*.data"),
                                     ("All files", "*.*") ))
                             )
    def onApply(self):
        if self.varFileName.get() != st.StaticType.UnkownName:
            self.winItemObject.outputFileName=self.varFileName.get()
        self.onCancel()
    
    def loadVariables(self):
        self.varFileName.set(self.winItemObject.outputFileName)
        
