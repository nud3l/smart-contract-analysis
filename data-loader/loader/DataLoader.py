from sqlalchemy.orm import sessionmaker
import logging

# Application imports
from models.sql_model import Owner, Repository, Code
from SolidityParser import SolidityParser
from config.Config import Config


class DataLoader:
    def __init__(self):
        # import configuration
        config = Config()

        # setup SQL database
        Session = sessionmaker(bind=config.engine)
        self.db = Session()

        # setup MongoDB
        self.mongo = config.client.code  # table in Mongo
        self.code_base = self.mongo.code_base  # collection in Mongo

        # load solidity parser
        self.parser = SolidityParser()

    def load_repository(self, repository_id):
        repository = self.db.query(Repository).filter(Repository.id == repository_id).first()
        return repository

    def load_owner(self, owner_id):
        owner = self.db.query(Owner).filter(Owner.id == owner_id).first()
        return owner

    @staticmethod
    def create_code_document(code, repository, owner, parsed_code):
        code_dict = dict()
        code_dict['_id'] = code.id
        code_dict['name'] = code.name
        code_dict['path'] = code.path
        code_dict['date_added'] = code.date_added
        code_dict['date_modified'] = code.date_modified
        code_dict['repository_id'] = repository.id
        code_dict['repository_name'] = repository.name
        code_dict['repository_full_name'] = repository.full_name
        code_dict['repository_html_url'] = repository.html_url
        code_dict['repository_description'] = repository.description
        code_dict['repository_owner_id'] = owner.id
        code_dict['repository_owner_login'] = owner.login
        code_dict['repository_owner_html_url'] = owner.html_url
        code_dict['code'] = parsed_code

        return code_dict

    def store_solidity_code(self, code):
        try:
            if not self.code_base.find_one({"_id": code.id}):
                repository = self.load_repository(code.repository_id)
                owner = self.load_owner(repository.owner_id)
                parsed_code = self.parser.parse(code.code)

                if repository and owner and parsed_code:
                    code_document = self.create_code_document(code, repository, owner, parsed_code)
                    self.code_base.insert_one(code_document)

                    logging.info("Code id {} stored in the database".format(code.id))
                    return

                logging.info("Code id {} not added to the database".format(code.id))

            logging.info("Code id {} already in MongoDB".format(code.id))
        except AttributeError as e:
            logging.error("{}: No code provided".format(e))
        except OverflowError as e:
            logging.error("{}: Failed on code id {}".format(e, code.id))

    def parse_database(self):
        logging.info("Started data loader")
        code = self.db.query(Code).all()

        for item in code:
            logging.debug("Trying to store code id {}".format(item.id))
            self.store_solidity_code(item)
        logging.info("Finished data loader")
