import os # create file path/join file path,for linux path create beacuse of linux only
import sys # sys is for system error
from src.logger import logging#import logger
from src.exception import CustomException#import exception
import pandas as pd # to read dataset
from sklearn.model_selection import train_test_split

from dataclasses import dataclass#it directly create variable name,when no us of any functanility

from src.components.data_transformation import DataTransformation # after wrote data transformation






## Intitialize the Data Ingetion Configuration

@dataclass #constructor
class DataIngestionconfig: # all the inputs required so create a sepate class
    train_data_path:str=os.path.join('artifacts','train.csv')#training datapath
    test_data_path:str=os.path.join('artifacts','test.csv')#test datapath
    raw_data_path:str=os.path.join('artifacts','raw.csv')# raw DATAPATH MEANS KEEPING THE COPY OF MAIN DATASET

## create a class for Data Ingestion
class DataIngestion : 
    def __init__(self): # my func
        self.ingestion_config=DataIngestionconfig()#giving 3 path inside this variable

    def initiate_data_ingestion(self):# now create my own func for logging purpose
        logging.info('Data Ingestion methods Starts')
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,# train and test datapath
                self.ingestion_config.test_data_path
            )
  
            
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)




## run data ingestion(for checking purpose)



if __name__=="__main__":
    obj=DataIngestion()
    train_data_path, test_data_path=obj.initiate_data_ingestion()#start reading the dataset and do train test split
    data_transformation=DataTransformation()# after wrote data transformation
    train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path, test_data_path)
    
    






    
   