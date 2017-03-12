from context import SolidityParser
from json import loads


class TestParser:
    def __init__(self):
        pass

    def test_solidity_parser_no_input(self):
        Parser = SolidityParser.SolidityParser()
        file_path = None
        assert Parser.parse(file_path) is None

    def test_solidity_parser_simple_input(self):
        Parser = SolidityParser.SolidityParser()
        file_path = "data/simple.sol"
        json_path = "data/simple.json"
        json_contract = loads(json_path)
        assert Parser.parse(file_path) is json_contract

    def test_solidity_parser_complex_input(self):
        Parser = SolidityParser.SolidityParser()
        file_path = "data/complex.sol"
        json_path = "data/complex.json"
        json_contract = loads(json_path)
        assert Parser.parse(file_path) is json_contract

    def test_solidity_parser_invalid_input(self):
        Parser = SolidityParser.SolidityParser()
        file_path = "data/invalid.sol"
        assert Parser.parse(file_path) is None

