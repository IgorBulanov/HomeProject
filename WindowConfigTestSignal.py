import numpy as np
import tkinter as tk
from tkinter import ttk
import radar.WindowConfigFileOutput as wcfo


class WindowConfigTestSignal(wcfo.WindowConfigFileOutput):
    def __init__(self,
                 parent=None,
                 frameTitle= "Test Signal Configurator",
                 winItemObject=None,
                 itemSet=None,
                 geometry="300x400+600+300",
                 *arg, **kw):
    
        super(WindowConfigTestSignal, self).__init__(parent=parent,
                                                    frameTitle= frameTitle,
                                                    winItemObject=winItemObject,
                                                    itemSet=itemSet,
                                                    geometry=geometry,
                                                    *arg, **kw)
        self.frameElementValue = ttk.Frame(self.top)
        self.frameElementValue.pack(side=tk.TOP, fill=tk.X, expand=False)

        frameSampling = ttk.Frame(self.top)
        frameSampling.pack(side=tk.TOP, fill=tk.X, expand=False)
        sampling_label=ttk.Label(frameSampling, text= "Sample rate:", width=15)
        sampling_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.varSampleRate=tk.DoubleVar()
        self.varSampleRate.set(100.0)
        sampling_entry = ttk.Entry(frameSampling, width=10, textvariable=self.varSampleRate)
        sampling_entry.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=2, pady=2)
        
        frameSampleLength = ttk.Frame(self.top)
        frameSampleLength.pack(side=tk.TOP, fill=tk.X, expand=False)
        sampleLength_label = ttk.Label(frameSampleLength, text= "Sample length:", width=15)
        sampleLength_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.varSampleLength=tk.DoubleVar()
        self.varSampleLength.set(4.0*np.pi)
        sampleLength_entry = ttk.Entry(frameSampleLength, width=10, textvariable=self.varSampleLength)
        sampleLength_entry.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=2, pady=2)

        framePerсentNoise = tk.Frame(self.top)
        framePerсentNoise.pack(side=tk.TOP, fill=tk.X, expand=False)
        perсentNoise_label = ttk.Label(framePerсentNoise, text= "Perсent noise:", width=15)
        perсentNoise_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.varPerсentNoise=tk.DoubleVar()
        self.varPerсentNoise.set(0.0)
        perсentNoise_entry = ttk.Entry(framePerсentNoise, width=10, textvariable=self.varPerсentNoise)
        perсentNoise_entry.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=2, pady=2)
        
        frameElementCount = ttk.Frame(self.top)
        frameElementCount.pack(side=tk.TOP, fill=tk.X, expand=False)
        elementCount_label = ttk.Label(frameElementCount, text= "Element count:", width=15)
        elementCount_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.varElementCount=tk.IntVar()
        self.varElementCount.set(1)
        elementCount_entry = ttk.Entry(frameElementCount, width=10, textvariable=self.varElementCount)
        elementCount_entry.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=2, pady=2)
        elementCount_button = ttk.Button(frameElementCount, text = "Create", command=self.onCreateElements)
        elementCount_button.pack(side=tk.RIGHT, fill=tk.X, expand=False, padx=2, pady=2)

        #self.loadVariables()

    def onCreateElements(self):
        # self.winItemObject.amp_freq_phase_coefficients[-1][0] - amplitude;
        # self.winItemObject.amp_freq_phase_coefficients[-1][1] - frequency;
        # self.winItemObject.amp_freq_phase_coefficients[-1][2] - phase
        self.winItemObject.amp_freq_phase_coefficients.clear()
        self.frameElementValue.destroy()
        self.frameElementValue = ttk.Frame(self.top)
        self.frameElementValue.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        for i in range(self.varElementCount.get()):
            self.winItemObject.amp_freq_phase_coefficients.append([tk.DoubleVar(), tk.DoubleVar(), tk.DoubleVar()])
            frame1=ttk.Frame(self.frameElementValue)
            frame1.pack(side=tk.TOP, fill=tk.X, expand=False)
            #
            amplitude_label = ttk.Label(frame1, text= "Amplitude:")
            amplitude_label.pack(side=tk.LEFT, padx=2, pady=2)
            amplitude_entry = ttk.Entry(frame1, width=10, textvariable=self.winItemObject.amp_freq_phase_coefficients[-1][0])
            amplitude_entry.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=2, pady=2)
            self.winItemObject.amp_freq_phase_coefficients[-1][0].set(1.0)
            #
            frequency_label = ttk.Label(frame1, text= "Frequency:")
            frequency_label.pack(side=tk.LEFT, padx=2, pady=2)
            frequency_entry = ttk.Entry(frame1, width=10, textvariable=self.winItemObject.amp_freq_phase_coefficients[-1][1])
            frequency_entry.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=2, pady=2)
            self.winItemObject.amp_freq_phase_coefficients[-1][1].set(1.0*(i+1))
            #
            phase_label = ttk.Label(frame1, text= "Phase:")
            phase_label.pack(side=tk.LEFT, padx=2, pady=2)
            phase_entry = ttk.Entry(frame1, width=10, textvariable=self.winItemObject.amp_freq_phase_coefficients[-1][2])
            phase_entry.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=2, pady=2)
            self.winItemObject.amp_freq_phase_coefficients[-1][2].set(0.0)
    
    def onApply(self):
        wcfo.WindowConfigFileOutput.onApply(self)   #call parrent method;
        self.winItemObject.signalDescriptor.setSamplerate(self.varSampleRate.get())
        self.winItemObject.signalDescriptor.setSamplelength(self.varSampleLength.get())
        self.winItemObject.signalDescriptor.setPerсentNoise(self.varPerсentNoise.get())
        self.onCancel()

    def loadVariables(self):
        #wcfo.WindowConfigFileOutput.loadVariables(self)    #another way to call parent method;
        super(WindowConfigTestSignal, self).loadVariables()
        #to get from signal descriptor;
        self.varSampleLength.set(self.winItemObject.signalDescriptor.samplelength)
        self.varSampleRate.set(self.winItemObject.signalDescriptor.samplerate)
        self.varPerсentNoise.set(self.winItemObject.signalDescriptor.perсentNoise)
        
        