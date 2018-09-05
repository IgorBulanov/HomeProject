class StaticType(object):
    UnkownName = "unknown"  #unknown name;
    # type name
    UnkownType = "unknown"
    FileType = "file"
    DataType = "dataSet"
    # do not forget to add new types into typeNameList
    typeNameList = [UnkownType,
                    FileType,
                    DataType]
    commentChar = "#"
    # (<mode-name>, <mode-code>)
    inputMode = ("read", "r")
    outputMode = ("write", "w")
    modeList = (inputMode, outputMode)
    # selector types of items;
    InputFile = "Input File"
    OutputFile = "Output File"
    Display = "- Item Display"
    Filter1 = "- Filter - 1"
    Filter2 = "- Filter - 2"
    TestSignal = "Test Signal"

    addItemList = [InputFile, OutputFile, Display, Filter1, Filter2, TestSignal]
    msg_not_saved = "Item is not saved\ndo not forget save changes...\n"
    #StaticType.msg_not_saved
    msg_data_set_was_builded="data set was builded"
    
    
    @staticmethod
    def selectTypeWindow():
        pass

