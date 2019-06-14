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

def print_popular_urls(urls_dataframe, number_to_report):
    """
    Prints the most popular URLs and how many times they have been clicked.
   
    urls_dataframe: pandas dataframe of url information, refreshed via
                    update command.
    number_to_report: number of urls to show data for.
    """
    most_popular_urls = urls_dataframe.sort_values("total_clicks", \
                                                  ascending=False)
    print("Your most popular urls were: \n")
    for i in range (0, number_to_report):
        try:
            print("%s with %i total click(s)." \
                  %(most_popular_urls.iloc[i].url, \
                  most_popular_urls.iloc[i].total_clicks))
        except:
            print("URL index requested exceeds total number of URLs.")


def print_popular_messages(messages_dataframe, number_to_report):
    """                                                                         
    Prints the most popular messages and how many times they have opened and
    how many opens are unique.
                                                                                
    messagess_dataframe: pandas dataframe of url information, refreshed via          
                    update command.                                             
    number_to_report: number of messages to show data for.                          
    """   
    most_popular_messages = messages_dataframe.sort_values("stats_total_opens", \
                                                            ascending=False)
    print("Your most popular messages were: \n")                                    
    for i in range (0, number_to_report):                                       
        try:                                                                    
            print("%s with %i total open(s) and %i unique open(s)." \
                  % (most_popular_messages.iloc[i].subject, \
                     most_popular_messages.iloc[i].stats_total_opens, \
                     most_popular_messages.iloc[i].stats_unique_opens))
        except:                                                                 
            print("Message index requested exceeds total number of messages.") 

def print_popular_subscribers(subs_dataframe, number_to_report):
    """                                                                         
    Prints the most engaged subscribers' email addresses, number of opens,
    number of unqiue opens, number of clicks, and number of unique clicks.     
                                                                                
    subs_dataframe: pandas dataframe of subscriber information, refreshed via          
                    update command.                                             
    number_to_report: number of subscribers to show data for.                          
    """   
    biggest_fans = subs_dataframe.sort_values("stats_total_opens", \
                                              ascending=False)
    print("Your biggest fan(s) were: \n")                                
    for i in range (0, number_to_report):                                       
        try:                                                                    
            print("%s with %i total open(s), %i unique open(s), %i total URL " \
                  "click(s), and %i unique URL click(s)." \
                  % (biggest_fans.iloc[i].email, \
                     biggest_fans.iloc[i].stats_total_opens, \
                     biggest_fans.iloc[i].stats_unique_opens, \
                     biggest_fans.iloc[i].stats_total_clicks, \
                     biggest_fans.iloc[i].stats_unique_clicks))
        except:                                                                 
            print("Message index requested exceeds total number of subscribers.")
