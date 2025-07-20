import requests
from pathlib import Path
import pandas as pd
from custom_logger import logger
from io import StringIO
import os

class APIWrapper:
    def __init__(self, api_address, api_port):
        self.api_address = api_address
        self.api_port = api_port
        self.base_url = r"http://" + self.api_address + ":" +str(self.api_port)
        logger.info(f"API wrapper created with Base endpoint: {self.base_url}")

        self.check_connection()

    def check_connection(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            logger.info("Connection to API successful.")
        except Exception as e:
            logger.error("Connection to API failed.")
            logger.error("-------------------------------------------------------------")
            logger.exception(e)
            logger.error("-------------------------------------------------------------")
            raise e


    def list_countries(self):
        endpoint = self.base_url + r"/list_countries"
        logger.info(f"Querying endpoint: {endpoint}")
        
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            results = response.json()
            return [x['country'] for x in results]
        except Exception as e:
            logger.error(f"Connection to endpoint failed: {endpoint}")
            logger.error("-------------------------------------------------------------")
            logger.exception(e)
            logger.error("-------------------------------------------------------------")
            raise e
            
    def country_data(self, countries=None):
        endpoint = self.base_url + r"/country_data"
        logger.info(f"Querying endpoint: {endpoint}")
        
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            
            data = pd.read_json(StringIO(response.text))
            if countries:
                data = data[data['country'].isin(countries)]
            return data
        except Exception as e:
            logger.error(f"Connection to endpoint failed: {endpoint}")
            logger.error("-------------------------------------------------------------")
            logger.exception(e)
            logger.error("-------------------------------------------------------------")
            raise e