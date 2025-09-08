class dockerML(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message=message
        
class modelError(dockerML):
    def __init__(self,message):
        super().__init__(message)
        
        
class predictorError(dockerML):
    def __init__(self,message):
        super().__init__(message)