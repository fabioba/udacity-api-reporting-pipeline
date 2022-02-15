"""
This module provides an API to run model on data to predict


Date: 15th of Feb, 2022
Author: Fabio Barbazza
"""


from socketserver import ThreadingUnixDatagramServer
from flask import Flask, request
import pandas as pd
import logging
import pickle

logging.basicConfig(format='%(funcName)s %(asctime)s %(message)s',level='INFO')
logger=logging.getLogger(__name__)



app = Flask(__name__)


def get_predicted_data(data):
    """
        Read model and return predicted data

        Args:
            data(pandas Dataframe):  input data
    """
    try:
        logger.info('START')
        
        # read model
        model=pickle.load(open('model/deployedmodel.pkl','rb'))

        predicts=model.predict(data)

        return predicts
    except Exception as err:
        logger.exception(err)
        raise

def predict(filename):
    """
        Predict data

        Args:
            filename(str): path of the input file
    """
    try:
        logger.info('START')
        input_data=pd.read_csv(filename)

        result=get_predicted_data(input_data)

        return result
    except Exception as err:
        logger.exception(err)



@app.route('/')
def index():
    return "Home \n"

@app.route('/prediction')
def prediction():
    filename = request.args.get('filename')
    predicted_data=predict(filename)
    return str(predicted_data)


app.run(host='0.0.0.0', port=8000)

