class dockerML(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message=message
        
class dataLoaderError(dockerML):
    def __init__(self,message):
        super().__init__(f"[DataLoaderError]: {message}")
        
        
class preprocessorError(dockerML):
    def __init__(self,message):
        super().__init__(f"[PreprocessorError]: {message}")