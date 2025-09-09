from app.data_loader import DataLoader
from app.exceptions import dataLoaderError

try:
    loader=DataLoader()
    data,target=loader.load_raw_data()
    print(data)
    print(target)
except dataLoaderError as e:
    print(e.message)