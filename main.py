import snscrape.modules.twitter as sntwitter
import pandas as pd             # dataframe construction
from datetime import date       # date range to run query over
import yaml                     # .yaml configuration file for input

def TwitterWebScraper(query_term, quantity, handle, filename, start_date, end_date):
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')

# Prepping strings that define search criteria
    handle_string = f'from:{handle}'
    filename_string = f'{filename}.csv'
    start_date_string = f'since:{start_date}'
    end_date_string = f'until:{end_date}'

    query_script = f'{query_term} {handle_string}  {start_date_string} {end_date_string}'
    search_filter = sntwitter.TwitterSearchScraper(query_script)
    web_data = []       
# tweet generator is iterated over
    for i, tweet in enumerate(search_filter.get_items()):
        if i > quantity: # amount of tweets
            break
        web_data.append([tweet.date, tweet.rawContent, tweet.user.username, f'{query_term}', tweet.retweetCount, tweet.likeCount, tweet.replyCount])
# Create dataframe
    dataframe = pd.DataFrame(web_data, columns=(['Date/Time', 'Text', 'Username', 'Query_Term', 'Retweet_Count', 'Like_Count', 'Reply_Count']))

    dataframe.to_csv(filename_string)  # Output to .csv format

    print(web_data)      # view raw data in terminal

# TwitterWebScraper() function demonstration :
# TwitterWebScraper('Apple', 500, 'business', 'example_filename', date(2006, 7, 15), date.today())

with open("YAML_Config.yaml", "r") as file:                 # You will need a .yaml file to run this 
    load_yaml = yaml.safe_load_all(file)
    for document in load_yaml:
        TwitterWebScraper(**document)



# Sentiment analysis on financial sector - GCP academic research project
