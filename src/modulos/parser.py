import pandas as pd

def __init__(self):
    """ load model """
    self.cols = ['test','testq']
        
def parser(request):
    file = request.files                   
    if file is not None:
        df = pd.read_csv(file.get('file'))
    return df
