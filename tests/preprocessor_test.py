from app.data_loader import DataLoader
from app.preprocessor import preprocessor
from app.exceptions import preprocessorError,dataLoaderError

try:
    loader=DataLoader()
    data,target=loader.load_raw_data()
    converter=preprocessor()
    transform_data=converter.fit_transform(data)
    print(transform_data)
    
except preprocessorError as e:
    print(e.message)
except dataLoaderError as e:
    print(e.message)
except Exception as e:
    print(str(e))