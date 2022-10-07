import pycaret
pycaret.__version__
from pycaret.classification import *

import pandas as pd

class Churn:
    
    def __init__(self):
        """ load model """
        self.model = load_model('models/best_pipeline')
        self.significado = ["Negativa","Positivo"]

    def predict(self,values:pd.DataFrame)-> dict:

       
        result = predict_model(self.model, data = values, round = 0)
        dt = result       

        return dt