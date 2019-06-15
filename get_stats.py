"""
Prints all-time stats for the newsletter. 
# TODO Port this to a web API :) 
"""
from utils import *

def all_time_stats(urls_to_report=10, messages_to_report=3, subscribers_to_report=10):
    """
    Reports basic all-time statistics of the blog, with some summary
    data for the top URLs, messages, and subscribers.

    number_to_report : The number of URLS to report statistics for.
    messages_to_report : The number of messages to report statistics for.
    subscribers_to_report : The number of subscribers to report statistics for.
    """
    # Create dataframes needed.
    urls_file = os.path.join(".", "url_data.csv")
    urls_dataframe = pandas.read_csv(urls_file)
    messages_file = os.path.join(".", "message_data.csv")
    messages_dataframe = pandas.read_csv(messages_file)
    subs_file = os.path.join(".", "sub_data.csv")
    subs_dataframe = pandas.read_csv(subs_file)

    # Print each set.
    print_popular_urls(urls_dataframe, urls_to_report)
    print("----------------------------------------------------------------\n")
    print_popular_messages(messages_dataframe, messages_to_report)
    print("----------------------------------------------------------------\n")
    print_popular_subscribers(subs_dataframe, subscribers_to_report)
