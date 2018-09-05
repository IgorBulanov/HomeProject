'''
Created on 2 мая 2018 г.

@author: Igor
'''
import tkinter as tk
from tkinter import messagebox
import radar.StaticType as st
import radar.SignalDescriptor as sd

class BaseItem(object):
    def __init__(self, auto_run = False,
                 runInThread=False,
                 typeName=st.StaticType.UnkownType,
                 dataSetName=st.StaticType.UnkownType,
                 sourceName=st.StaticType.UnkownName,
                 itemSet=None,
                 *arg, **kw ):

        self.dataSet = []                   # result data;
        self.amp_freq_phase_coefficients = [] # self.serialFactorVaule[-1][0] - amplitude; [-1][1] - frequency; [-1][2] - phase
        self.dataSetName = dataSetName      # name of dataSet in ItemSet;
        self.typeName = typeName            # name of this item type;
        self.auto_run = auto_run            # toggle to run in auto_run mode;
        self.run_in_thread = runInThread    # toggle to run in thread mode;
        self.sourceName = sourceName        # dataSetName to get source data;
        self.displayName = ""               # name of display item;
        self.itemSet = itemSet              # pointer to container of items;
        self.signalDescriptor = sd.SignalDescriptor(dataSet=self.dataSet)
        super(BaseItem, self).__init__()    #*arg, **kw

    def append(self, e):                    # to add to internal data set;
        self.dataSet(e)
    def setAutoRun(self, autoRun = True):   # set toggle of auto run;
        self.auto_run = autoRun
    def getAutoRun(self):                   # get value of auto run toggle;
        return self.auto_run
    def setRunInThread(self, runInThread = True): # set multithread toggle;
        self.run_in_thread = runInThread
    def getRunInThread(self):               # get value of multithread toggle;
        return self.run_in_thread
    def setTypeName(self, tn):
        self.typeName = tn
    def getTypeName(self):                  # get type name;
        return self.typeName
    def getDataSetName(self):               # get dataSetName;
        return self.dataSetName
    def isTypeNameValid(self, t):           # probe: is type name valid?
        return t in st.StaticType.typeNameList
    def setSourceName(self, sourceName):    # set source name;
        self.sourceName = sourceName
    def getSourceName(self):                # get source name;
        return self.sourceName
    def autoRun(self):                      # autoRun method;
        if self.auto_run :
            self.run()
    def run(self):
        pass
    def getSourceItemByName(self):
        return self.itemSet.getItemByName(self.sourceName)



