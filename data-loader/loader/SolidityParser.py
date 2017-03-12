import subprocess
import json
from os import path


class SolidityParser:
    def __init__(self):
        current_path = path.dirname(path.realpath(__file__))
        self.parser_path = "{}/../node_modules/.bin/solidity-parser".format(current_path)

    def parse(self, file_path):
        if file_path:
            try:
                json_raw = subprocess.Popen(
                        [self.parser_path, file_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                )
                # json_raw = subprocess.check_output([self.parser_path, file_path])
                json_code = json.loads(json_raw.communicate()[0])

                return json_code

            except ValueError as e:
                print "{}: Invalid Solidity code file".format(e)

        return None

# node_modules/.bin/solidity-parser /home/nud3l/GitHub/Dinvest/solidity/contracts/HedgeContract1.sol