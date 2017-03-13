import yaml
from pkg_resources import resource_string
import logging
from sqlalchemy import create_engine
from pymongo import MongoClient


class Config(object):
    def __init__(self):
        file_path = resource_string(__name__, 'config.yml')
        with open(file_path, 'r') as ymlfile:
            config = yaml.load(ymlfile)

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

