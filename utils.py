"""
Utility functionality for tinyletter tools. Useful mainly for getting, 
storing, and processing data from the tinyletter server.
# TODO Add debugging statements if verbose = true
"""

import argparse                                                                 
import getpass                                                                  
import os                                                                       
import pandas                         
import tinyapi  

def pull_data():
    """
    Leverage existing tinyapi functionality to get data from the letters.
    Stores the subscriber, draft, message, and url data to separate csv files.

    Those files store the subscriber, url, message, and draft data in separate
    csv files called "sub_data.csv," "url_data.csv," "message_data.csv," 
    and "draft_data.csv" respectively after filtering and flattening
    each dataset. 

    Note that the user will need to provide the tinyletter username and 
    password via CLI. This can be modified, but should be done in a way
    that promotes personal account security. 
    """

    username = input("Username: ")
    tinyletter = tinyapi.Session(username, getpass.getpass())

    # Pull relevant data tables from the tinyletter server.
    subscriber_data = tinyletter.get_subscribers()
    url_data = tinyletter.get_urls()
    message_data = tinyletter.get_messages()
    draft_data = tinyletter.get_drafts()

    # Filter out unnecessary columns and flatten out the data.
    filtered_sub = process_subscribers(subscriber_data)
    filtered_url = process_urls(url_data)
    filtered_message = process_messages(message_data)
    filtered_draft = process_drafts(draft_data)

    # Name each csv file.
    sub_file = os.path.join(".", "sub_data.csv")
    url_file = os.path.join(".", "url_data.csv")
    message_file = os.path.join(".", "message_data.csv")
    draft_file = os.path.join(".", "draft_data.csv")

    # Save all of the filtered data to respective CSV files.
    pandas.DataFrame(filtered_sub).to_csv(sub_file, encoding="utf8")
    pandas.DataFrame(filtered_url).to_csv(url_file, encoding="utf8")
    pandas.DataFrame(filtered_message).to_csv(message_file, encoding="utf8")
    pandas.DataFrame(filtered_draft).to_csv(draft_file, encoding="utf8")

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

    return subscriber_data


def process_urls(url_data, verbose=True, csv_filename="url_data.csv"):
    """
    Processes raw url data output from tinyletter servers - removes any private
    authentictation artifacts, flattens, and makes into readable (and 
    parseable!) csv file.

    TODO Investigate what can be removed here and remove it.
    """
    print(flatten(url_data))
    return url_data

def process_messages(message_data, verbose=True, message_filename="message_data,csv"):
    """
    Processes raw url data output from tinyletter servers - removes any private 
    authentictation artifacts, flattens, and makes into readable (and           
    parseable!) csv file.                                                       
                                                                                
    TODO Investigate what can be removed here and remove it.  
    """
    pass

def process_drafts(draft_data, verbose=True, drafts_filename="draft_data.csv"):
    """
    Processes raw url data output from tinyletter servers - removes any private 
    authentictation artifacts, flattens, and makes into readable (and           
    parseable!) csv file.                                                       
                                                                                
    TODO Investigate what can be removed here and remove it.  
    """
    pass

def flatten(dictionary, separator='_', prefix=''):                                 
    # Code heavily adopted from https://stackoverflow.com/a/19647596/4280216.
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dictionary.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dictionary, dict) else { prefix : dictionary}
