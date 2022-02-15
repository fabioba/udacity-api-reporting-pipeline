"""
This module provides an API call


Date: 15th of Feb, 2022
Author: Fabio Barbazza
"""

import requests
import logging


logging.basicConfig(format='%(funcName)s %(asctime)s %(message)s',level='INFO')
logger=logging.getLogger(__name__)

def get_prediction():
    try:
        response=requests.get('http://127.0.0.1:8000/prediction?filename=data/predictiondata.csv')

        if response.status_code==200: 
            predicts=response.content
        else:
            raise KeyError('status!=200')


        return predicts
    except Exception as err:
        logger.exception(err)


if __name__=='__main__':
    PREDICTS=get_prediction()

    logger.info('PREDICTS: {}'.format(PREDICTS))