#!/usr/bin/env python3
"""
CLI interface for utility functions.
"""


import argparse
import getpass
import os
import pandas as pd
import tinyapi

from utils import *


def main():
    """
    Offers command-line options for pulling and working with that 
    sweet treasure trove of tinyletter data.
    """
    commands = argparse.ArgumentParser()
    commands.add_argument("-u", "--update-data", help="Pulls data down \
                          from the tinyletter servers, processes it, and \
                          stores it in CSV files.", 
                          action="store_true");
    commands.add_argument("-a", "--all-time-stats", help="Gives all time stats
                          from every issue.") 
    commands.add_argument("-i", "--issue-stats", help="Gives stats for
                          some issue i of the newsletter (0-indexed.")
    arguments = commands.parse_args()
    if arguments.pulldata:
        pull_data()
    if arguments.all-time-stats:
        all_time_stats()
    if arguments.latest_stats:
        itemized_stats()

if __name__ == '__main__':
    main()
