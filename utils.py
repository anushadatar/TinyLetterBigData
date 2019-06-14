"""
Utility functionality for tinyletter tools. Useful mainly for getting, 
storing, and processing data from the tinyletter server.
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

def process_subscribers(subscriber_data, csv_filename="subscriber_data.csv"):
    """
    Processes raw subscriber data output from tinyletter servers - removes
    private keys and similar data, flattens and makes into readable (and 
    parseable!) csv file.
    
    The subscriber data is a list of dictionaries for each subscriber where
    each dict has two major additional subdicts : one with statistics about 
    their interaction with the newsletter and one with their personal data.  
    We're not a big tech company, so we can't get away with messing with
    personal data, so we will just remove that information.
    
    The final .csv file will have a column with the email address  of each user
    and a column with the 'stats' dictionary for them with nothing ommitted.
    """
    # Omit unneeded columns, feel free to add or remove deletions as needed.
    for subscriber in subscriber_data:
        del subscriber['data']
        del subscriber['is_new']
        del subscriber['key']
        del subscriber['__methods']
        del subscriber['__model'] 
        del subscriber['updated_at']
        del subscriber['created_at']
        del subscriber['__id']
    subscriber_data_filtered = [flatten(sub) for sub in subscriber_data]
    return subscriber_data_filtered

def process_urls(url_data, verbose=True, csv_filename="url_data.csv"):
    """
    Processes raw url data output from tinyletter servers - removes any private
    authentictation artifacts, flattens, and makes into readable (and 
    parseable!) csv file.
    """
    # Omit unneeded columns, feel free to add or remove deletions as needed.
    for url in url_data:
        del url['__id']
        del url['__methods']
        del url['__model']
        del url['stub']
        del url['unique_clicks']
    return url_data

def process_messages(message_data, verbose=True, message_filename="message_data,csv"):
    """
    Processes raw url data output from tinyletter servers - removes any private 
    authentictation artifacts, flattens, and makes into readable (and           
    parseable!) csv file.                                                       
    """
    # Omit unneeded columns, feel free to add or remove deletions as needed. 
    for message in message_data:
        del message['__id']
        del message['__methods']
        del message['__model']
        del message['created_at']
        del message['public_message']
        del message['queue_count']
        del message['scheduled_at']
        del message['snippet']
        del message['status']
        del message['to_list']
        del message['tweet_id']
        del message['updated_at']
        del message['stub']
    message_data_filtered = [flatten(mes) for mes in message_data]        
    return message_data_filtered

def process_drafts(draft_data, verbose=True, drafts_filename="draft_data.csv"):
    """
    Processes raw url data output from tinyletter servers - removes any private 
    authentictation artifacts, flattens, and makes into readable (and           
    parseable!) csv file.                                                       
    """
    return (draft_data)

def flatten(dictionary, separator='_', prefix=''):                                 
    """
    Helper method to turn subdictionaries into additional columns.
    
    dictionary: Dictionary to separate
    separator: Delimeter for new headers.
    prefix: Start for new headers.
    
    ode heavily adopted from https://stackoverflow.com/a/19647596/4280216.
    """
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dictionary.items()
             for k, v in flatten(vv, separator, kk).items()
             } if isinstance(dictionary, dict) else { prefix : dictionary}
