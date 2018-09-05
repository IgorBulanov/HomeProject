import radar.BaseItem as BaseItem
import radar.StaticType as st

class FileType(BaseItem):
    def __init__(self, auto_run = False,
                 runInThread = False,
                 dataSetName=st.StaticType.UnkownName,
                 sourceName=st.StaticType.UnkownName,
                 *arg, **kw ):
        self.delimiter = ""
        self.fileName = ""
        self.mode = FileType.inputMode
        self.fileIsOpen = False
        
        super(FileType, self).__init__(auto_run = auto_run,
                                       runInThread = runInThread,
                                       typeName=st.StaticType.FileType,
                                       dataSetName=dataSetName,
                                       sourceName=sourceName,
                                       *arg, **kw )
    
    def setMode(self, m):
        self.mode = m
    def getMode(self):
        return self.mode
    def getModeName(self):
        return self.mode[0]
    def getModeCode(self):
        return self.mode[1]
    def getModeByName(self, modeName=st.StaticType.inputMode[0]):
        for e in st.StaticType.modeList:
            if e[0] == modeName:
                return e
        return None
    def setFileName(self, fileName):
        self.fileName = fileName
    def getFileName(self):
        return self.fileName
    def setDelimiter(self, delimiter=""):
        self.delimiter = delimiter
    def getDelimiter(self):
        return self.delimiter
    def read(self):
        try:
            with open(self.fileName, self.getModeCode() ) as file_handler:
                for line in file_handler:
                    line.strip()
                    if line[0] == st.StaticType.commentChar:
                        continue    # skip comment line;
                    x,y=line.split()
                    self.append( (float(x), float(y)) )
            file_handler.close()
        except IOError:
            tk.messagebox.showerror("Error", "An IOError has occurred!\n"+
                                    "file: "+self.fileName+"\n"+
                                    "not found!")
    
    def write(self):
        try:
            with open(self.fileName, st.StaticType.outputMode[1] ) as file_handler:
                for e in self.dataSet:
                    line = "{} {}".format(e[0], e[1])
                    file_handler.write(line)
            file_handler.close()
        except IOError:
            tk.messagebox.showerror("Error", "An IOError has occurred!\n"+
                                    "in file: "+self.fileName+"\n")

