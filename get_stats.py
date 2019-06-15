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

def itemized_stats(urls_to_report=10):
    """
    Reports basic statistics for a given issue of the blog, with some summary
    data for the top URLs and most interested subscribers.
    """
    message_number = int(input("Which message number would you like data for?"))

    # Create dataframes needed.                                                 
    urls_file = os.path.join(".", "url_data.csv")                               
    urls_dataframe_full = pandas.read_csv(urls_file)                                 
    messages_file = os.path.join(".", "message_data.csv")                       
    messages_dataframe_full = pandas.read_csv(messages_file)                         
    subs_file = os.path.join(".", "sub_data.csv")                               
    subs_dataframe_full = pandas.read_csv(subs_file)                                 
       
    # Get and filter by the unique message id for each issue.
    message_list = messages_dataframe_full.sort_values("sent_at", ascending=True)
    specified_message = message_list.iloc[message_number-1]
    query = "message_id == %i" % (specified_message.id)
    urls_dataframe = urls_dataframe_full.query(query)

    print("Your message %s had %i total opens and %i unique opens. This is an open rate of %s" \
                                         % (specified_message.subject, \
                                         specified_message.stats_total_opens, \
                                         specified_message.stats_unique_opens, \
                                         specified_message.stats_open_rate) ) 
    print("----------------------------------------------------------------\n") 
    print_popular_urls(urls_dataframe, urls_to_report)                          
