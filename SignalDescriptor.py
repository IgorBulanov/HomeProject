import math

class SignalDescriptor(object):
    '''
        samplerate - Hz
        frequency - Hz
        volume - v
        samplelength -sec
    '''
    id_samplerate="SampleRate"
    id_samplelength="SampleLength"
    id_perсentNoise="PerсentNoise"
    def __init__(self,
                 samplerate=1.0,
                 amplitude=1.0,
                 frequency=1.0,
                 phase=0.0,
                 samplelength=1.0,
                 perсentNoise=0.0,
                 dataSet = [],
                 *args, **kwargs):
        self.dataSet = dataSet
        self.samplerate = samplerate
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase=phase
        self.samplelength = samplelength
        self.perсentNoise = perсentNoise
        super(SignalDescriptor, self).__init__(*args, **kwargs)
        
    def getSampleDelta(self):
        return 1.0/self.samplerate
    
    def getCountSample(self):
        return int(self.samplelength/self.getSampleDelta())
    
    def getPeriod(self):
        return self.samplerate/self.frequency/2
    
    def setPerсentNoise(self, perсentNoise):
        self.perсentNoise = perсentNoise
        
    def setSamplerate(self, samplerate=0.0):
        self.samplerate = samplerate

    def setFrequency(self, frequency=1.0):
        self.frequency = frequency
        
    def setAmplitude(self, amplitude=1.0):
        self.amplitude = amplitude

    def setSamplelength(self, samplelength):
        self.samplelength = samplelength

    def createDataSet(self, f):
        cs = self.getCountSample()
        delta=self.getSampleDelta()
        for i in range(0, cs):
            x=i*delta
            self.dataSet.append((x, f(x)))
            
