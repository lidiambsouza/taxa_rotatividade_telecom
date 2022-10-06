import pycaret
pycaret.__version__
from pycaret.classification import *

import pandas as pd

class Churn:
    
    def __init__(self):
        """ load model """
        self.model == load_model('best_pipeline')
        self.significado = ["Negativa","Positivo"]

    def predict(self,values:pd.DataFrame)-> dict:

        """
        Classificar se a pessoa tem diabetes [Positivo] 
        ou não [Negativo]

        Retorna
            Um dicionário contendo o resultado da classificação

        """

       
        result = predict_model(self.model, data = values, round = 0)

        output = {'results': self.significado[int(result.Label[0])]}

        return output