from app.predictor import predictor
from app.exceptions import dataLoaderError,preprocessorError,modelError,trainerError,predictorError


try:
    predictor=predictor()
    ans=predictor.predict([1.2,3.4,1.5,2.9])
    print(ans)
except dataLoaderError as e:
            print(str(e))            
except preprocessorError as e:
            print(str(e))             
except modelError as e:
            print(str(e))          
except trainerError as e:
            print(str(e))          
except predictorError as e:
            print(str(e))          
except Exception as e:
            print(str(e))  