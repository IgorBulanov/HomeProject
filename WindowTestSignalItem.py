import math
import radar.StaticType as st
import radar.WindowBase4Item as wb4i
import radar.WindowConfigTestSignal as wcts
import radar.WindowFileOutputItem as wfoi

class WindowTestSignalItem(wfoi.WindowFileOutputItem):
    def __init__(self,
                 parent = None,
                 frameTitle= "Test Signal Item",
                 itemSet = None,
                 geometry="300x400+600+300",
                 *args, **kw):
        self.parent = parent
        #self.itemSet = itemSet
        self.frameTitle = frameTitle
        self.geometry = geometry
        
        super(WindowTestSignalItem, self).__init__(parent=self.parent,
                                                   frameTitle=self.frameTitle,
                                                   itemSet = itemSet,
                                                   geometry=self.geometry,
                                                   *args, **kw)

    def onConfig(self):
        wb4i.WindowBase4Item.onConfig(self) #output warning message only;
        c=wcts.WindowConfigTestSignal(parent=self.parent, frameTitle="Test Signal Configurator",
                          winItemObject=self, itemSet=self.itemSet, geometry=self.geometry) #"400x400+400+300"
        c.loadVariables()
    
    def onRun(self):
        '''
        for c in self.amp_freq_phase_coefficients:
            print("amplitude={} frequency={} phase={}".format( c[0].get(), c[1].get(), c[2].get()) )
        '''
        self.dataSet.clear()
        self.signalDescriptor.createDataSet(self.func)
        '''
        # debug only
        for (x, y) in self.dataSet:
            print("x={} y={}".format(x, y))
        '''
        wfoi.WindowFileOutputItem.onRun(self)   #run parent method onRun - write data list into file;
        self.messageOut(st.StaticType.msg_data_set_was_builded)

    def func(self, x):
        # self.serialFactorVaule[-1][0] - amplitude; [-1][1] - frequency; [-1][2] - phase
        y=0
        for k in self.amp_freq_phase_coefficients:
            y=y+k[0].get()*math.cos( k[1].get()*x+k[2].get() )
        return y


    


