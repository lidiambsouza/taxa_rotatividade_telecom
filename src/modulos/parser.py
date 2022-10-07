from ast import Not
import numpy as np
import pandas as pd

def __init__(self):
    """ load model """
    self.cols = ['test','testq']
        
def parser(request):
   """ features = [x for x in request.form.values()]
   final = np.array(features)
   data_unseen = pd.DataFrame([final], columns= self.cols) """
   file = request.files                   
   if file is not None:
       df = pd.read_csv(file.get('file'))
   return df