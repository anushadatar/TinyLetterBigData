#!/usr/bin/env python3

import argparse
import getpass
import os
import pandas as pd
import tinyapi

from pull_data import *


def main():
    """
    Offers command-line options for pulling and working with that 
    sweet treasure trove of tinyletter data.
    """
    commands = argparse.ArgumentParser()
    # TODO Add individual type support for pulling data via CLI.
    commands.add_argument("-p", "--pulldata", help="Pulls data down \
                          from the tinyletter servers, processes it, and \
                          stores it in CSV files.", 
                          action="store_true");
    arguments = commands.parse_args()
    if arguments.pulldata:
        pull_data()

if __name__ == '__main__':
    main()
