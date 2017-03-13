# Data Loader
The data loader scans through a SQL database of Solidity contracts crawled from GitHub. To receive the data using the GitHub API you may refer to my [github-crawler repository](https://github.com/nud3l/github-search-crawler). This will download Solidity contracts to your system and store their metadata in a SQL DB.

The contract files are parsed with the [ConsenSys solidity parser](https://github.com/ConsenSys/solidity-parser). The contract metadata from GitHub and to codefiles are stored into a MongoDB to analyse their code.

## Installation
- Make sure to have a PostgreSQL DB setup and filled with data as explained in the [github-crawler repository](https://github.com/nud3l/github-search-crawler).
- Install MongoDB on your system with this [tutorial](https://docs.mongodb.com/manual/installation/).
- This installation procedures assumes NVM is installed on your system. If not you can follow the instructions [here](https://github.com/creationix/nvm).
- From the `data-loader` folder install the solidity parser with `npm install solidity-parser`.
- Create a Python virtual environment and activate it. If you don't know how, follow the [tutorial](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
- Build and install the python project from the shell with the activated virtual environment with `python setup.py build` and `python setup.py install`.

## Execute the loader
Run `python loader` with your activated virtual environment. The loader will take all contracts stored in the SQL database and store their GitHub data and the parsed contract code in MongoDB. It checks if a specific contract is already added to the DB and skip adding it, if that is the case. It may run for quite a while, depending on the amount of contracts. You can `tail -f log/data-loader.log` to see the progress.

## Known issues
Sometimes `.sol` files on GitHub are actually not Solidity files or the Solidity files contain errors. In that case, they are not added in MongoDB and an error is logged.

In some cases the compiled code contains some large integers (great than 8 byte). These can not be handled by MongoDB and the code will not be added. An error is logged.
