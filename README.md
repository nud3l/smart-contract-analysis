# Smart contract analysis for Solidity
This repository automatically analyses solidity contract files for specific characteristics. The intention is to quantify these characteristics  to give an overview of the current state of Solidity development.

## Dateset
The dataset of solidity contracts that I have used for this analysis is compiled from public GitHub repositories. To receive the data using the GitHub API you may refer to my [github-crawler repository](https://github.com/nud3l/github-search-crawler). This will download Solidity contracts to your system and store their metadata in a SQL DB.

## Characteristics

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
  -
