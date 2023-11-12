import os
import sys
import pickle # for creating a pickel file from model
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):# create a func which taking the path of the pickel file
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:# wb means read bight mode
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)