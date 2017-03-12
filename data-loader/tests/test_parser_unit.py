from context import SolidityParser
import json
from os import path

class TestParser:
    def test_solidity_parser_no_input(self):
        Parser = SolidityParser.SolidityParser()
        file_path = None
        assert Parser.parse(file_path) is None

    def test_solidity_parser_simple_input(self):
        Parser = SolidityParser.SolidityParser()

        current_path = path.dirname(path.realpath(__file__))
        file_path = "{}/data/simple.sol".format(current_path)
        json_path = "{}/data/simple.json".format(current_path)

        with open(json_path) as data_file:
            stored_contract = json.load(data_file)
        created_contract = Parser.parse(file_path)

        # sort the JSONs to allow for comparison
        stored_contract = json.dumps(stored_contract, sort_keys=True)
        created_contract = json.dumps(created_contract, sort_keys=True)

        assert created_contract == stored_contract

    def test_solidity_parser_complex_input(self):
        Parser = SolidityParser.SolidityParser()

        current_path = path.dirname(path.realpath(__file__))
        file_path = "{}/data/complex.sol".format(current_path)
        json_path = "{}/data/complex.json".format(current_path)

        with open(json_path) as data_file:
            stored_contract = json.load(data_file)
        created_contract = Parser.parse(file_path)

        # sort the JSONs to allow for comparison
        stored_contract = json.dumps(stored_contract, sort_keys=True)
        created_contract = json.dumps(created_contract, sort_keys=True)

        assert created_contract == stored_contract

    def test_solidity_parser_invalid_input(self):
        Parser = SolidityParser.SolidityParser()

        current_path = path.dirname(path.realpath(__file__))
        file_path = "{}/data/invalid.sol".format(current_path)
        assert Parser.parse(file_path) is None

