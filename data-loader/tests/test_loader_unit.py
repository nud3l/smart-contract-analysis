from context import DataLoader
from models.sql_model import Owner, Repository, Code

class TestLoader:
    def test_load_repository_no_input(self):
        loader = DataLoader.DataLoader()
        assert loader.load_repository(None) is None

    def test_load_repository_valid_input(self):
        loader = DataLoader.DataLoader()
        repository_test = loader.db.query(Repository).first()
        repository = loader.load_repository(repository_test.id)
        assert repository == repository_test

    def test_load_repository_not_found(self):
        loader = DataLoader.DataLoader()
        repository_id = 0
        assert loader.load_repository(repository_id) is None

    def test_load_owner_no_input(self):
        loader = DataLoader.DataLoader()
        assert loader.load_owner(None) is None

    def test_load_owner_valid_input(self):
        loader = DataLoader.DataLoader()
        owner_test = loader.db.query(Owner).first()
        owner = loader.load_owner(owner_test.id)
        assert owner == owner_test

    def test_load_owner_not_found(self):
        loader = DataLoader.DataLoader()
        owner_id = 0
        assert loader.load_owner(owner_id) is None

    def test_store_solidity_code_no_input(self):
        loader = DataLoader.DataLoader()
        code = None
        assert loader.store_solidity_code(code) is None

    def test_store_solidity_code_valid_code(self):
        loader = DataLoader.DataLoader()
        code = loader.db.query(Code).first()
        assert loader.store_solidity_code(code) is None
