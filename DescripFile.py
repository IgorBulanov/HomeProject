
class DescripFile(object):
    keyTime="T"
    keyFrequency="F"
    keyDuration="D"
    keyComment="\# "
    keyDelimiter="="
    keyNL="\n"
    def __init__(self, time=0.0, frequency=0.0, duration=0.0):
        self.descriptor={}
        self.descriptor.update({DescripFile.keyTime:time,
                         DescripFile.keyFrequency:frequency,
                         DescripFile.keyDuration:duration
                         })
        
    def getTime(self):
        return self.descriptor[DescripFile.keyTime]

    def getFrequency(self):
        return self.descriptor[DescripFile.keyFrequency]

    def getDuration(self):
        return self.descriptor[DescripFile.keyDuration]

    def getAll(self):
        return (self.getTime(), self.getFrequency(), self.getDuration())

    def getHeader(self):
        return DescripFile.keyComment+DescripFile.keyTime+DescripFile.keyDelimiter+self.getTime()+DescripFile.keyNL+\
               DescripFile.keyComment+DescripFile.keyFrequency+DescripFile.keyDelimiter+self.getFrequency()+DescripFile.keyNL+\
               DescripFile.keyComment+DescripFile.keyDuration+DescripFile.keyDelimiter+self.getDuration()+DescripFile.keyNL
    
    def setHeaderValue(self, s):
        pass
    
    @classmethod
    def class_method(cls, x):
        pass

    @staticmethod
    def static_method(x):
        pass
