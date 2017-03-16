import yaml
import os
import logging
from sqlalchemy import create_engine
from pymongo import MongoClient


class Config(object):
    def __init__(self):
        file_path = os.path.dirname(os.path.realpath(__file__))
        with open("{}/config.yml".format(file_path), 'r') as ymlfile:
            config = yaml.load(ymlfile)
	
	# create a log directory
        if not os.path.exists("log"):
            os.makedirs("log")

        # create SQL connection
        sql = config['sql']
        self.engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
                sql['user'],
                sql['password'],
                sql['host'],
                sql['port'],
                sql['db']
        ))

        # create MongoDB connection
        mongo = config['mongo']
        self.client = MongoClient(mongo['host'], int(mongo['port']))

        # setup logging
        log_file = config['log']['file']
        logging.basicConfig(
                filename=log_file,
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%d/%m/%Y %I:%M:%S %p'
        )

