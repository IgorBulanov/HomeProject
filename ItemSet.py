import tkinter as tk
import radar.BaseItem as bi
import radar.StaticType as st
import radar.WindowBase4Item as wbi

class ItemSet(object):
    def __init__(self, *arg, **kw):
        self.unitSet = []
        super(ItemSet, self).__init__(*arg, **kw)
    
    def getIndexByName(self, name):
        for i, e in enumerate(self.unitSet):
            if e.dataSetName == name:
                return i
        return None
    
    # get BaseItem by DataSetName
    def getItemByName(self, name):
        for e in self.unitSet:
            if e.getDataSetName() == name:
                return e
        return None
    def saveItemIntoUnitSet(self, e):
        if isinstance(e, wbi.WindowBase4Item):
            i = self.getIndexByName(e.dataSetName)  # get item by name from list;
            if i == None:                           # the name is not present then add item;
                self.unitSet.append(e)              # add item to unitSet list;
                e.messageOut("item was appended.")  # display status message;
            else:
                self.unitSet.pop(i)                 # item is present: to remove i-th item from list;
                self.unitSet.append(e)              # add item to unitSet list;
                e.messageOut("item was updated.")   # display status message;
        else:
            tk.messagebox.showinfo("Warning", "only BaseItem allowed to store") #show type error message;

