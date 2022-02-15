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


def get_predicted_data(filename):
    """
        Read model and return predicted data

        Args:
            filename(str): path of the input file
    """
    try:
        logger.info('START')
        predict_data=pd.read_csv(filename)


        return 
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
        predict_data=pd.read_csv(filename)


        return 
    except Exception as err:
        logger.exception(err)



@app.route('/')
def index():
    user = request.args.get('user')
    return "Hello " + user + '\n'

@app.route('/prediction')
def prediction():
    filename = request.args.get('filename')
    thedata=readpandas(filename)
    return str(len(thedata.index))


app.run(host='0.0.0.0', port=8000)

