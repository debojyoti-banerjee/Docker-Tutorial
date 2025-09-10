from app.trainer import trainer
from app.exceptions import dataLoaderError,preprocessorError,modelError,trainerError

try:
    train=trainer()
    train.train_and_save()
except dataLoaderError as e:
            print(str(e))            
except preprocessorError as e:
            print(str(e))             
except modelError as e:
            print(str(e))          
except Exception as e:
            print(str(e))  