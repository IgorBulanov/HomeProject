import radar.BaseItem as BaseItem
import radar.StaticType as st

class DataSetType(BaseItem):
    def __init__(self, auto_run = False,
                 runInThread = False,
                 dataSetName=st.StaticType.UnkownName,
                 sourceName=st.StaticType.UnkownName,
                 *arg, **kw ):
        
        super(DataSetType, self).__init__(auto_run = auto_run,
                                          runInThread = runInThread,
                                          typeName=st.StaticType.DataType,
                                          dataSetName=dataSetName,
                                          sourceName=sourceName,
                                          *arg, **kw )


