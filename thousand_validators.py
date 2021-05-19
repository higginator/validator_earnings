from flask import json
import requests

"""
    Returns a list of validators in the Polkadot 1000 Validators Programme.
    Example:
    [
        {
          "kusamaStash":"HngUT2inDFPBwiey6ZdqhhnmPKHkXayRpWw9rFj55reAqvi",
          "name": "specialized-tarmac-1",
          "riotHandle": "@joe:web3.foundation",
          "stash": "126RwaHn4MDekLWfUYfiqcVbiQHapwDSAT9vZZS15HLqfDJh"
        }, ...
    ]
"""
def get_polkadot_validators():
    # raw source file of the validators in the Polkadot Thousand Validators Programme
    url = 'https://raw.githubusercontent.com/w3f/1k-validators-be/master/helmfile.d/config/polkadot/otv-backend.yaml.gotmpl'
    return get_validator_json(url)

"""
    Returns a list of validators in the Kusama 1000 Validators Programme.
    Example:
    [
        {
            "name": "ryanhigs",
            "riotHandle": "@ryanhigs:matrix.org",
            "stash": "HLsh79QY2bnA5URc9jrxwwH6xvnqbzU59HDpgrJNgwLsdct"
        }, ...
    ]
"""
def get_kusama_validators():
    # raw source file of the validators in the Kusama Thousand Validators Programme
    url = 'https://raw.githubusercontent.com/w3f/1k-validators-be/master/helmfile.d/config/kusama/otv-backend.yaml.gotmpl'
    return get_validator_json(url)

"""
    Returns a list of validators in the 1000 Validators Programme, at the specified URL.
    Example:
    [
        {
          "kusamaStash":"HngUT2inDFPBwiey6ZdqhhnmPKHkXayRpWw9rFj55reAqvi",
          "name": "specialized-tarmac-1",
          "riotHandle": "@joe:web3.foundation",
          "stash": "126RwaHn4MDekLWfUYfiqcVbiQHapwDSAT9vZZS15HLqfDJh"
        }, ...
    ]
"""
def get_validator_json(url):
    # get the source file
    raw_text = requests.get(url).text
    # get the JSON in the file
    config_start = raw_text.find('config')
    json_start_offset = raw_text[config_start:].find('{')
    json_start = config_start + json_start_offset
    json_string = raw_text[json_start:]
    json_string_stripped = json_string.replace('\n','')
    # remove db data from string, it is malformed JSON
    db_start_index = json_string_stripped.find('db')
    matrix_start_index = json_string_stripped.find('matrix')
    json_string_db_removed = json_string_stripped[:db_start_index] + json_string_stripped[matrix_start_index:]
    # load the json
    all_json = json.loads(json_string_db_removed)
    # return the validators
    return all_json['scorekeeper']['candidates']
