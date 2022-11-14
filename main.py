#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Giffen Good"
__version__ = "0.1.0"
__license__ = "MIT"

import os
import argparse
from dotenv import load_dotenv, find_dotenv
from connections import Psql
from constants import OXFORD_ID, OXFORD_SECRET
from dictionary import WordFactory, OxfordDictionary
from util import write_response_to_file, set_cli_args
from constants import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

load_dotenv(find_dotenv())


def main(cli_args):
    """ Main entry point of the app """
    oxford_dict = OxfordDictionary("https://od-api.oxforddictionaries.com:443/api/v2", OXFORD_ID,
                                   OXFORD_SECRET)

    db = Psql(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

    w = WordFactory.create_word(cli_args.word, cli_args.base_lang, cli_args.target_lang, oxford_dict, db)
    res = WordFactory.run_cmd(w, cli_args.cmd)

    if res:
        write_response_to_file(w, cli_args, res)
    else:
        print('No results found')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()
    args = set_cli_args(parser, __version__)
    main(args)

# print(json.dumps(trans, indent = 4))
