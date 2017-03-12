import subprocess


class SolidityParser:
    def __init__(self):
        self.parser_path = "../node_modules/.bin/solidity-parser"

    def parse(self, file_path):
        if file_path:
            command = "{} {}".format(self.parser_path, file_path)

            try:
                json_code = subprocess.check_call(command, shell=True)

                return json_code

            except:
                

        return None

# node_modules/.bin/solidity-parser /home/nud3l/GitHub/Dinvest/solidity/contracts/HedgeContract1.sol