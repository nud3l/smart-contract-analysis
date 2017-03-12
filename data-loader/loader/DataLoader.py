from config import Config
from sqlalchemy.orm import sessionmaker
from model import Repository, Owner, Code, metadata


class DataLoader:
    def __init__(self):
        # import configuration
        self.config = Config()

        # setup the database
        Session = sessionmaker(bind=self.config.engine)
        metadata.create_all(self.config.engine, checkfirst=True)
        self.db = Session()
