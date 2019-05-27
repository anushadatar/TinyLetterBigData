"""
Utility functionality for tinyletter tools. Useful mainly for getting, 
storing, and processing data from the tinyletter server.
"""

import argparse                                                                 
import getpass                                                                  
import os                                                                       
import pandas as pd                                                             
import tinyapi  

def pull_data():
    """
    Leverage existing tinyapi functionality to get data from the letters.
    Stores the subscriber, draft, message, and url data to separate csv files.
    """
    username = input("Username: ")
    tinyletter = tinyapi.Session(username, getpass.getpass())

    # Pull relevant data tables from the tinyletter server.
    subscriber_data = tinyletter.get_subscribers()
    url_data = tinyletter.get_urls()
    message_data = tinyletter.get_messages()
    draft_data = tinyletter.get_drafts()

    process_subscribers(subscriber_data)
    process_urls(url_data)
    process_messages(message_data)
    process_drafts(draft_data)

def process_subscribers(subscriber_data, verbose=True, csv_filename="subscriber_data.csv"):
    """
    Processes raw subscriber data output from tinyletter servers - removes
    private keys and similar data, flattens and makes into readable (and 
    parseable!) csv file.
    """
    # The subscriber data is a list of dictionaries for each subscriber where
    # each dict has two major additional subdicts : one with statistics about 
    # their interaction with the newsletter and one with their personal data.  
    # We don't really have (or really want) personal data, so we can just 
    # remove that information to simplify our records.
    for subscriber in subscriber_data:
        del subscriber['data']
        del subscriber['key']
    # Flatten out fields in the dictionary.
    subscriber_data = flatten(subscriber_data)

    print(subscriber_data)


def process_urls(url_data, verbose=True, csv_filename="url_data.csv"):
    """
    Processes raw url data output from tinyletter servers - removes any private
    authentictation artifacts, flattens, and makes into readable (and 
    pareable!) csv file.
    """
    pass

def process_messages(message_data, verbose=True, message_filename="message_data,csv"):
    """
    """
    pass

def process_drafts(draft_data, verbose=True, drafts_filename="draft_data.csv"):
    """
    """
    pass

def flatten(dictionary, separator='_', prefix=''):                                 
    # Code heavily adopted from https://stackoverflow.com/a/19647596/4280216.
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dictionary.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dictionary, dict) else { prefix : dictionary}
