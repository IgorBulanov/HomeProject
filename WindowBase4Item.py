import tkinter as tk
from tkinter import ttk
import radar.BaseItem as bi
import radar.StaticType as st
from random import randint
import radar.WindowSelectSourceDataSet as wssds
import radar.WindowConfig as wc

import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

#mpl.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure

class WindowBase4Item(bi.BaseItem):
    def __init__(self,
                 parent = None,
                 frameTitle= "",
                 itemSet = None,
                 *args, **kw):
        self.parent = parent
        self.frameTitle = frameTitle
        self.mainFrame = ttk.LabelFrame(self.parent, text=self.frameTitle)
        #self.itemSet = itemSet
        super(WindowBase4Item, self).__init__(  auto_run = False,
                                                runInThread = False,
                                                typeName=st.StaticType.UnkownType,
                                                dataSetName=st.StaticType.UnkownType,
                                                sourceName=st.StaticType.UnkownName,
                                                itemSet = itemSet,
                                                *args, **kw)
        self.mainFrame.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.itemFrame = ttk.Frame(self.mainFrame)
        self.itemFrame.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.buttonFrame = ttk.Frame(self.mainFrame)
        self.buttonFrame.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
        
        #dataSetName
        f_dsn = ttk.Frame(self.itemFrame)
        f_dsn.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.dataSetName_label = ttk.Label(f_dsn, text="Data set name:")
        self.dataSetName_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.varDataSetName=tk.StringVar()
        self.dataSetName_entry = ttk.Entry(f_dsn, textvariable=self.varDataSetName)
        self.varDataSetName.set("Item-"+str(randint(0, 99)))
        self.dataSetName_entry.pack(side=tk.LEFT, fill=tk.X, padx=2, pady=2)
        
        #sourceName
        f_sn = ttk.Frame(self.itemFrame)
        f_sn.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.sourceName_label = ttk.Label(f_sn, text= "Source Name:  ")
        self.sourceName_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.varSourceName=tk.StringVar()
        self.sourceName_entry = ttk.Entry(f_sn, textvariable=self.varSourceName)
        self.sourceName_entry.pack(side=tk.LEFT, fill=tk.X, padx=2, pady=2)
        self.varSourceName.set(st.StaticType.UnkownName)
        self.button_select_sourceName = ttk.Button(f_sn,
                                                   text = "Select", command=self.selectSourceName)
        self.button_select_sourceName.pack(side=tk.LEFT, expand=False)
        
        #displayName
        frameDisplayName = ttk.Frame(self.itemFrame)
        frameDisplayName.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.displayName_label = ttk.Label(frameDisplayName, text= "Display Name:  ")
        self.displayName_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.varDisplayName=tk.StringVar()
        self.displayName_entry = ttk.Entry(frameDisplayName, textvariable=self.varDisplayName)
        self.displayName_entry.pack(side=tk.LEFT, fill=tk.X, padx=2, pady=2)
        self.varDisplayName.set("Display Name-"+str(randint(0, 99)))
        
        #typeNameDataSet
        f2 = ttk.LabelFrame(self.itemFrame, text="Select type of item")
        f2.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.varCodeTypeName = tk.IntVar()
        self.varCodeTypeName.set(1)
        n=1
        for e in st.StaticType.typeNameList:
            #command=self.selectItem
            if e != st.StaticType.UnkownType:
                rb = tk.Radiobutton(f2,
                                    text=e, indicatoron = 0, width = 10,
                                    variable=self.varCodeTypeName, value=n,
                                    command=lambda x=st.StaticType.msg_not_saved: self.messageOut(x))
                rb.pack( anchor = tk.W )
                n+=1
        
        #auto_run
        f3 = ttk.LabelFrame(self.itemFrame, text="Run config")
        f3.pack(side=tk.TOP, fill=tk.X, expand=True)
        
        self.var_auto_run = tk.BooleanVar()
        self.var_auto_run.set(False)
        self.check_auto_run = ttk.Checkbutton(f3, text="Auto run",
                                              variable=self.var_auto_run, command=self.onClickAutoRun)
        self.check_auto_run.pack(side=tk.LEFT, padx=2, pady=2)
        
        #run_in_thread
        self.var_run_in_thread = tk.BooleanVar()
        self.var_run_in_thread.set(False)
        self.check_run_in_thread = ttk.Checkbutton(f3, text="Run in thread",
                                                   variable=self.var_run_in_thread,command=self.onClickRunInThread)
        self.check_run_in_thread.pack(side=tk.RIGHT, padx=2, pady=2)
        
        #message frame:
        self.message_var = tk.StringVar()
        self.message_frame = ttk.LabelFrame(self.itemFrame, text="Message")
        self.message_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
        self.message_label = ttk.Label(self.message_frame, textvariable=self.message_var)
        self.message_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.message_var.set(st.StaticType.msg_not_saved)
        
        # button frame:
        self.button_config_item = ttk.Button(self.buttonFrame, text = "Config", command=self.onConfig)
        self.button_config_item.pack(side=tk.LEFT)
        self.button_close_item = ttk.Button(self.buttonFrame, text = "Save", command=self.onSave)
        self.button_close_item.pack(side=tk.LEFT)
        self.button_run_item = ttk.Button(self.buttonFrame, text = "Run", command=self.onRun)
        self.button_run_item.pack(side=tk.LEFT)
        self.button_display_item = ttk.Button(self.buttonFrame, text = "Display", command=self.onDisplay)
        self.button_display_item.pack(side=tk.LEFT)
    
    def selectSourceName(self):
        self.messageOut(st.StaticType.msg_not_saved)
        type_name = self.getTypeName()
        if type_name == st.StaticType.DataType:
            sn = wssds.WindowSelectSourceDataSet(winItemObject=self, parent=self.parent, itemSet=self.itemSet)
            return
        if type_name == st.StaticType.FileType:
            self.varSourceName.set( tk.filedialog.askopenfilename(initialdir = ".",
                                                                title = "Select file",
                                                                filetypes = (("data files","*.*"),("all files","*.*")))
                                    )
            return
        
    def onConfig(self):
        self.messageOut(st.StaticType.msg_not_saved)
        
    def onSave(self):
        self.dataSetName = self.varDataSetName.get()
        self.sourceName = self.varSourceName.get()
        self.typeName = st.StaticType.typeNameList[self.varCodeTypeName.get()]
        self.auto_run = self.var_auto_run.get()
        self.run_in_thread = self.var_run_in_thread.get()
        # debug only:
        #print("dataSetName={}".format(self.dataSetName))
        self.itemSet.saveItemIntoUnitSet(self)
        
    def onRun(self):
        pass

    def onDisplay(self):
        # status: ok
        f = Figure(figsize=(5,4), dpi=100)
        a = f.add_subplot(111)
        a.plot(x, y)

        #draw_frame = ttk.Frame(self.itemSet.parent4drawFrame)
        #draw_frame.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas = FigureCanvasTkAgg(f, master=self.itemSet.parent4drawFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, anchor=tk.W, fill=tk.X, expand=False)
    
        '''
        # debug only
        draw_label = ttk.Label(self.itemSet.parent4drawFrame, text= "on pressed button display: Draw label")
        draw_label.pack(side=tk.LEFT, padx=2, pady=2)
        '''

    def onDisplay2(self):
        # [x for t in a for x in t]
        #
        # a = [(1,2), (3,4), (5,6)]
        # x = [i[0] for i in a]
        # y = [i[1] for i in a]
        x = [i[0] for i in self.dataSet]
        y = [i[1] for i in self.dataSet]

        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(211, facecolor='#FFFFCC')

        ax.plot(x, y, '-')
        ax.set_ylim(-2, 2)
        ax.set_title('Press left mouse button and drag to test')

        ax2 = fig.add_subplot(212, facecolor='#FFFFCC')
        line2, = ax2.plot(x, y, '-')

        def onselect(xmin, xmax):
            indmin, indmax = np.searchsorted(x, (xmin, xmax))
            indmax = min(len(x) - 1, indmax)
    
            thisx = x[indmin:indmax]
            thisy = y[indmin:indmax]
            line2.set_data(thisx, thisy)
            ax2.set_xlim(thisx[0], thisx[-1])
            ax2.set_ylim(min(thisy), max(thisy))
            fig.canvas.draw()

        # set useblit True on gtkagg for enhanced performance
        span = SpanSelector(ax, onselect, 'horizontal', useblit=True,
                            rectprops=dict(alpha=0.5, facecolor='red'))
        
        plt.show()
        
    def onClickAutoRun(self):
        pass
    def onClickRunInThread(self):
        pass
    def messageOut(self, msg):
        self.message_var.set(msg)



