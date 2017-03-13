# Smart contract analysis for Solidity
This repository automatically analyses solidity contract files for specific characteristics. The intention is to quantify these characteristics to give an overview of the current state of Solidity development.

## Dataset
The dataset of solidity contracts used for this analysis is compiled from public GitHub repositories. To receive the data using the GitHub API you may refer to the [github-crawler repository](https://github.com/nud3l/github-search-crawler). This will download Solidity contracts to your system and store their metadata in a SQL DB.

## Structure of this repository
- analysis: This includes an jupyter notebook with the analytics performed on the Solidity Contracts
- data-loader: A Python module to load the GitHub data into MongoDB. See specific instructions in the folders README file

To get up and running with the jupyter notebook, make sure to follow the installation instructions in the data-loader folder. Additionally, you need to install the following packages via pip:
- jupyter
- matplotlib (this will take some time)

## Characteristics
Details are in the jupyter notebook. The characteristics include for example:
- Metadata
  - Solidity version of the contract
  - Name of the contract
- Contract variables, structs, and events
  - Number of variables
  - Number of structs
  - Number of mappings
  - Number of events
- Contract modifiers
  - Number of modifiers
- Contract functions
  - Number of functions
  - Number of informal parameters per function
