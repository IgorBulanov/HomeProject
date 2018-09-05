import sys
import tkinter as tk
from tkinter import ttk
import radar.WindowBase4Item as wb4i
import radar.WindowConfigFileOutput as wcfo
import radar.StaticType as st

class WindowFileOutputItem(wb4i.WindowBase4Item):
    def __init__(self,
                 parent = None,
                 frameTitle= "File Output Item",
                 itemSet = None,
                 *args, **kw):
        self.parent = parent
        #self.itemSet = itemSet
        self.frameTitle = frameTitle
        super(WindowFileOutputItem, self).__init__(parent=parent,
                                                  frameTitle=frameTitle,
                                                  itemSet = itemSet,
                                                  *args, **kw)
        self.outputFileName=st.StaticType.UnkownName
        

    def onConfig(self):
        wb4i.WindowBase4Item.onConfig(self) #display warning message only;
        c=wcfo.WindowConfigFileOutput(parent=self.parent, frameTitle="File Output Configurator",
                          winItemObject=self, itemSet=self.itemSet, geometry="400x200+400+300",)
        c.loadVariables()

    def onSave(self):
        wb4i.WindowBase4Item.onSave(self)   #replace item into itemset;
    
    def onRun(self):
        try:
            F=open(self.outputFileName, "w")
            F.writelines( ["{0} {1}\n".format(i[0],i[1]) for i in self.dataSet] )
            #for c in self.dataSet:
                # F.write("{0} {1}".format(c[0], c[1]))
        except IOError as err:
            print("I/O error: {0}".format(err))
        finally:
            F.close()




