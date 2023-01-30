import snscrape.modules.twitter as sntwitter
from tqdm import tqdm
import requests as rq
import markovify
import nltk

from util_funcs import f_disc_time, f_time

import os, re, json










# Class to make the model more accurate
class POSifiedText(markovify.NewlineText):
	def word_split(self, sentence):
		words = re.split(self.word_split_pattern, sentence)
		words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
		return words

	def word_join(self, words):
		sentence = " ".join(word.split("::")[0] for word in words)
		return sentence












def init_config(config_dir:str, config_fp:str, data_dir:str, data_fp:str, colors:dict) -> dict:
    """
    It checks if the config directory and data directory exist, if they don't, it creates them. Then it
    checks if the config file exists, if it doesn't, it creates it. Then it creates the data file. Then
    it reads the config file and returns it
    
    :param config_dir: The directory where the config file is located
    :type config_dir: str
    :param config_fp: The filepath to the config file
    :type config_fp: str
    :param data_dir: The directory where the data file is stored
    :type data_dir: str
    :param data_fp: The filepath to the data file
    :type data_fp: str
    :return: A dict of the config.json file
    """
    res, log, war, spe = colors['res'], colors['log'], colors['war'], colors['spe']

    # Log the config dir, config file, data dir, and data file
    print(f'{log}[LOG]      {res}Config directory: {spe}{config_dir}{res}')
    print(f'{log}[LOG]      {res}Config file:      {spe}{config_fp}{res}')
    print(f'{log}[LOG]      {res}Data directory:   {spe}{data_dir}{res}')
    print(f'{log}[LOG]      {res}Data file:        {spe}{data_fp}{res}')

    # Checks if config dir exists
    if os.path.exists(config_dir):
        print(f'{log}[LOG]      {res}{spe}{config_dir}{res} exists')
    # If it doesnt, creates it
    else:
        print(f'{war}[WARNING]{res}  {spe}{config_dir}{res} does not exist. Creating it')
        os.makedirs(config_dir)

    # Checks if data dir exists
    if os.path.exists(data_dir):
        print(f'{log}[LOG]    {res}  {spe}{data_dir}{res} exists')
    # If it doesnt, creates it
    else:
        print(f'{war}[WARNING]{res}  {spe}{data_dir}{res} does not exist. Creating it')
        os.makedirs(data_dir)
    
    # Checks if config file exists
    if os.path.exists(config_fp):
        print(f'{log}[LOG]    {res}  {spe}{config_fp}{res} exists')
    # If it doesnt, creates an empty config.json
    else:
        print(f'{war}[WARNING]{res}  {spe}{config_fp}{res} does not exist. Creating it')
        with open(config_fp, 'w') as f:
            json.dump({ 'reddit':{'username':''} , 'discord':{'token':''} , 'twitter':{'username':''} }, f, indent=4)
    
    # Checks if data file exists
    if os.path.exists(data_fp):
        print(f'{log}[LOG]    {res}  {spe}{data_fp}{res} exists')
    # If it doesnt, creates an empty data file
    else:
        print(f'{log}[LOG]    {res}  {spe}{data_fp}{res} does not exist. Creating it')
        with open(data_fp, 'w') as f:
            json.dump({}, f)

    # Reads config.json and returns it
    with open(config_fp) as f:
        config = json.load(f)
    
    return config
        














def do_reddit(config:dict, data_fp:str, colors:dict):
    """
    It scrapes the comments of a user from reddit via pushshift.io, and saves them to the data file
    
    :param config: The config file
    :type config: dict
    :param data_fp: The file path to the data file
    :type data_fp: str
    :param colors: A dictionary containing the colors for the terminal
    :type colors: dict
    """
    res, log, war, spe = colors['res'], colors['log'], colors['war'], colors['spe']

    # Checks if all the required info is present
    present = False
    if config.get('reddit'):
        if config.get('reddit').get('username'):
            present = True
    # If it isnt given, warns the user and skips reddit
    if not present:
        print(f'{war}[WARNING]{res}  Reddit username not given, so {spe}skipping reddit{res}')
        return

    # Gets the username of the user
    username = config['reddit']['username']
    url      = f'https://api.pushshift.io/reddit/comment/search/?author={username}&order=desc&sort_type=created_utc&size=100'
    print(f'{log}[LOG]      {res}Getting the newest reddit comments of {spe}u/{username}{res}')
    # Scrapes the comments
    comments = []
    pbar     = tqdm(total=10000, leave=False, colour='#696969')
    # The loop keeps going until either the limit (10k) is reached, or all the comments are scraped
    l_time   = None
    count    = 0
    while True:
        # Checks if we have enough data
        if len(comments) >= 10000:    break
        # Forms the new url
        new_url  = f'{url}&before={l_time}' if l_time else url
        r        = rq.get(new_url)
        new_data = r.json()
        # Checks if the new data was empty, meaning all comments are scraped
        if not new_data['data']:      break
        # Goes thro the new data
        for dic in new_data['data']:
            comments.append({
                'content':    dic.get('body'),
                'subreddit':  dic.get('subreddit'),
                'upvotes':    dic.get('score'),
                'timestamp':  dic.get('created_utc'),
                'id':         dic.get('id'),
                'url':        f'https://reddit.com{dic.get("permalink")}'
            })
            # Updates the last time (l_time) var, so that earlier comments can be scraped
            l_time = dic.get('created_utc') if dic.get('created_utc') else l_time        
            # Updates the progress bar & count
            pbar.update(1)
            count += 1
    # Closes the progress bar
    pbar.close()
    print(f'{log}[LOG]      {res}Collected {spe}{count}{res} comments')

    
    # Gets the already existing data
    with open(data_fp) as f:
        data = json.load(f)
    # Adds the collected comments to it
    data['reddit'] = comments
    # Saves the data
    with open(data_fp, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f'{log}[LOG]      {res}Saved the data to {spe}{data_fp}{res}')
















def do_discord(config:dict, data_fp:str, colors:dict):
    """
    It logs into discord, gets all the DM channels, gets all the messages in those channels, and saves
    them to a file
    
    :param config: The config dictionary
    :type config: dict
    :param data_fp: The file path to the data file
    :type data_fp: str
    """
    res, log, war, spe = colors['res'], colors['log'], colors['war'], colors['spe']

    # Checks if all the required info is present
    present = False
    if config.get('discord'):
        if config.get('discord').get('token'):
            present = True
    # If it isnt given, warns the user and skips discord
    if not present:
        print(f'{war}[WARNING]{res}  Discord token not given, so {spe}skipping discord{res}')
        return

    token = config['discord']['token']
    # Defines the headers to use in all the requests
    headers = {
        'Content-Type'  : 'application/json',
        'User-Agent'    : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Authorization' : token
        }
    # Gets basic data of the user
    print(f'{log}[LOG]      {res}Logging into discord')
    r        = rq.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
    username = r.get('username')
    disc     = r.get('discriminator')
    my_id    = r.get('id')
    # Checks if the token is valid
    if not my_id:
        print(f'{war}[WARNING]{res}  Discord token is invalid, so {spe}skipping discord{res}')
        return
    # Else, prints the username
    print(f'{log}[LOG]      {res}Logged in as {spe}{username}#{disc}{res} ({my_id})')

    # Gets all the DMs
    print(f'{log}[LOG]      {res}Getting all the DM channels')
    r        = rq.get(f'https://discordapp.com/api/v9/users/@me/channels', headers=headers).json()
    # Gets all the channel IDs
    chan_ids = []
    for chan_dic in r:    chan_ids.append(chan_dic['id'])

    # Goes thro the channel IDs
    new_data = []
    count    = 0
    print(f'{log}[LOG]      {res}Scraping the messages in the channels')
    for chan_id in tqdm(chan_ids, leave=False, colour='#696969'):
        # Gets the messages of the channel
        r = rq.get(f'https://discordapp.com/api/v9/channels/{chan_id}/messages?limit=100', headers=headers).json()
        # Goes thro the messages
        for msg in r:
            # Checks if message is a text message, is sent by us, and contains atleast smth
            if msg['type'] == 0 and msg['author']['id'] == my_id and msg['content']:
                # Adds all the needed attributes
                new_data.append({
                    'content':     msg['content'],
                    'timestamp':   f_disc_time( msg['timestamp'] ),
                    'channel_id':  chan_id,
                    'id':          msg['id'],
                    'url':         f'https://discord.com/channels/@me/{chan_id}/{msg["id"]}'
                })
                count += 1
    # Prints how many messages were collected from how many DMs
    print(f'{log}[LOG]      {res}Collected {spe}{count}{res} messages from {spe}{len(chan_ids)}{res} DM channels')

    # Gets the already existing data
    with open(data_fp) as f:
        data = json.load(f)
    # Adds the collected messages to it
    data['discord'] = new_data
    # Saves the data
    with open(data_fp, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f'{log}[LOG]      {res}Saved the data to {spe}{data_fp}{res}')
                














def do_twitter(config:dict, data_fp:str, colors:dict, max_twts:int=10000):
    """
    It scrapes the tweets of the user specified in the config file, and saves them to the data file
    
    :param config: The configuration file
    :type config: dict
    :param data_fp: The path to the data file
    :type data_fp: str
    :param max_twts: The maximum number of tweets to scrape, defaults to 10000
    :type max_twts: int (optional)
    """
    res, log, war, spe = colors['res'], colors['log'], colors['war'], colors['spe']

    # Checks if all the required info is present
    present = False
    if config.get('twitter'):
        if config.get('twitter').get('username'):
            present = True
    # If it isnt given, warns the user and skips twitter
    if not present:
        print(f'{war}[WARNING]{res}  Twitter username not given, so {spe}skipping twitter{res}')
        return

    # Gets the username
    username = config['twitter']['username']
    # Forms the query
    query    = sntwitter.TwitterSearchScraper(f'from:{username}').get_items()
    print(f'{log}[LOG]      {res}Scraping the tweets of {spe}@{username}{res}')
    # Scrapes the tweets
    tweets = []
    pbar   = tqdm(total=10000, leave=False, colour='#696969')
    count  = 0
    for twt in query:
        # Checks if we have enough tweets
        if count >= max_twts:    break
        # Adds all the required attributes
        tweets.append({
            'content':      twt.content,
            'timestamp':    twt.date.timestamp(),
            'likes':        twt.likeCount,
            'replies':      twt.replyCount,
            'retweets':     twt.retweetCount,
            'quote_tweets': twt.quoteCount,
            'id':           twt.id,
            'url':          twt.url
        })
        count += 1
        pbar.update(1)
    # Once done, closes the progressbar
    pbar.close()
    print(f'{log}[LOG]      {res}Collected {spe}{count}{res} tweets')

    # Gets the already existing data
    with open(data_fp) as f:
        data = json.load(f)
    # Adds the collected comments to it
    data['twitter'] = tweets
    # Saves the data
    with open(data_fp, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f'{log}[LOG]      {res}Saved the data to {spe}{data_fp}{res}')

    















def make_model(data_fp:str, colors:dict) -> POSifiedText:
    """
    It loads the data, extracts the useful text from it, and builds the model
    
    :param data_fp: The filepath to the data
    :type data_fp: str
    :return: A POSifiedText object
    """
    res, log, err = colors['res'], colors['log'], colors['err']

    # Loads the data
    with open(data_fp) as f:
        data:dict = json.load(f)

    # Gets all the useful sentences
    texts = []
    # Gets the keys of data, like "reddit", "discord" etc
    for platform in data.keys():
        # Gets the element (which is a dick), since data[platform] is a list
        for elem in data[platform]:
            # Extracts the useful text from it and adds it to the list
            text = elem['content']
            texts.append(text)
    
    # Checks if less then 100 texts are given
    if len(texts) < 100:
        print(f'{err}[ERROR]    Not enough data collected, must have atleast 100 texts/comments/tweets{res}')
        exit()
    
    # Builds the model
    print(f'{log}[LOG]      {res}Building the model')
    model = POSifiedText(texts)
    # # Complies it since on github it said that this should improve quality
    # model = model.compile() # This one for some reason doesnt produce readable sentences even though it should be the same as the next line. Remind me to open up an issue on github
    model.compile(inplace=True)

    return model














def generate_sentences(model:POSifiedText, colors:dict, count:int=50):
    """
    It generates a sentence, gets the color, and prints the sentence
    
    :param model: The model to use to generate the sentences
    :type model: POSifiedText
    :param count: The number of sentences to generate, defaults to 50
    :type count: int (optional)
    """
    # res, log, spe = colors['res'], colors['log'], colors['spe']

    print('\n\n\n')
    # All the colors the text can be
    colors = ['cyan1', 'yellow2']
    for i in range(count):
        # Generates a new sentence
        gen_sent = model.make_short_sentence(max_chars=280, tries=1000)
        # Gets the color
        index = i % len(colors)
        color = colors[index]
        # Prints the sentence
        print('-'*100)
        print(f'{gen_sent}')
    print('-'*100)















def print_stats(data_fp:str, count:int, start:int, end:int, colors:dict):
    """
    It prints the stats of the data collected
    
    :param data_fp: The filepath to the data collected
    :type data_fp: str
    :param count: the amount of sentences to generate
    :type count: int
    :param start: the time the program started
    :type start: int
    :param end: the time the program ended
    :type end: int
    :param colors: a dictionary containing the colors to use for the output
    :type colors: dict
    """
    res2, bol, spe = colors['res2'], colors['bol'], colors['spe']

    # Gets all the data collected
    with open(data_fp) as f:
        data:dict = json.load(f)
    # Gets the amount of messages collected of each platform
    red_count  = 0 if not data.get('reddit')  else len(data['reddit'])
    disc_count = 0 if not data.get('discord') else len(data['discord'])
    twt_count  = 0 if not data.get('twitter') else len(data['twitter'])
    total      = sum([red_count, disc_count, twt_count])
    # gets the time taken
    time_taken = f_time( int(end - start) )
    # Prints the stats
    print(f'''\n\n{bol}Done! Collected a total of {spe}{total}{res2} messages/posts, in which there were {spe}{red_count}{res2} \
reddit comments, {spe}{disc_count}{res2} discord messages, and {spe}{twt_count}{res2} tweets. Generated {spe}{count}{res2} \
sentences using that data

Total time taken: {spe}{time_taken}{res2}''')



        














'''
BLUEPRINT

(config)
Check if the config dir exists
If not, make it
Check if config file exists
If not, make an empty json file
read & return the config
'''