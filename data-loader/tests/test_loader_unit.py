from context import DataLoader


class TestLoader:
    def test_load_repository_no_input(self):
        loader = DataLoader.DataLoader()
        assert loader.load_repository(None) is None

    def test_load_repository_valid_input(self):
        loader = DataLoader.DataLoader()
        repository_id = 18150101
        repository = loader.load_repository(repository_id)
        assert repository.full_name == "ahirner/ethereum"

    def test_load_repository_not_found(self):
        loader = DataLoader.DataLoader()
        repository_id = 10
        assert loader.load_repository(repository_id) is None

    def test_load_repository_no_input(self):
        loader = DataLoader.DataLoader()
        assert loader.load_repository(None) is None

    def test_load_repository_valid_input(self):
        loader = DataLoader.DataLoader()
        repository_id = 18150101
        repository = loader.load_repository(repository_id)
        assert repository.full_name == "ahirner/ethereum"

    def test_load_repository_not_found(self):
        loader = DataLoader.DataLoader()
        repository_id = 10
        assert loader.load_repository(repository_id) is None
