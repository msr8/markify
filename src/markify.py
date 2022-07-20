print('Importing modules...')
from main_funcs import init_config, do_reddit, do_discord, do_twitter, make_model, generate_sentences, print_stats
from util_funcs import get_user, get_config_dir

from colorama import init as color_init
from colorama import Fore, Style

from argparse import ArgumentParser
import platform as pf
import time as t




def parse_the_fookin_args():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config',  type=str,  help='The path to config file. By default, its {LOCALAPPDATA}/markone/config.json on windows, and ~/.config/markone/config.json on other operating systems')
    parser.add_argument('-d', '--data',    type=str,  help='The path to the json data file. If given, the program will not scrape any data and will just compile the model and generate sentences')
    parser.add_argument('-n', '--number',  type=int,  help='Number of sentences to generate. Default is 50', default=50)
    args = parser.parse_args()
    return args













def main(args, colors:dict):
    res, log, spe = colors['res'], colors['log'], colors['spe']
    # Starts the time
    start = t.perf_counter()
    # Gets the initial stuff for program (os type, username, config stuff)
    SYSTEM = pf.system()
    USR    = get_user()
    CONFIG_DIR, CONFIG_FP, DATA_DIR, DATA_FP = get_config_dir(SYSTEM, USR, args)
    CONFIG = init_config(CONFIG_DIR, CONFIG_FP, DATA_DIR, DATA_FP, colors)
    # IF CONFIG FILE IS GIVEN VIA CLI
    # Prints out the available keys
    # -------------------- Todo
    keys = [f'{spe}{k}{res}' for k in CONFIG.keys()]
    print(f'{log}[LOG]    {res} Config keys: {", ".join(keys)}')
    # If data file is not given, scrapes the data
    if not args.data:
        do_reddit(CONFIG,  DATA_FP, colors)
        do_discord(CONFIG, DATA_FP, colors)
        # do_twitter(CONFIG, DATA_FP, colors)
    # Makes the model
    model = make_model(DATA_FP, colors)
    # Generates the sentences
    generate_sentences(model, colors, args.number)
    # Prints the stats
    end = t.perf_counter()
    print_stats(DATA_FP, args.number, start, end, colors)
    








    
def init_main():
    color_init()
    # Gets the colors
    COLORS = {
        'res'  : Style.RESET_ALL,
        'res2' : Fore.RESET,
        'bol'  : Style.BRIGHT,
        'log'  : Style.BRIGHT + Fore.LIGHTGREEN_EX,
        'war'  : Style.BRIGHT + Fore.LIGHTYELLOW_EX,
        'spe'  : Fore.LIGHTMAGENTA_EX
    }
    args = parse_the_fookin_args()
    main(args, COLORS)



if __name__ == '__main__':
    init_main()


























'''
BLUEPRINT


TODO
-> Make CLI accept -c
-> Add text in --help
-> Change bar format
-> Write checks in every main func
-> Fix discord timestamp





3 files:
  main.py
  util_funcs.py
  main_funcs.py


The program:
  Config stuff
  Check cli input with the following params:
    count
    data
    config

    reddit
    discord
    twitter
  Make the model
  Generate sentences
  In the end, print stats



config gonna be like:
{
    "reddit": {
        "username": ""
    },
    "discord": {
        "token": ""
    },
    "twitter": {
        "username": ""
    }
}



Data file gonna be like:
{
    "reddit": [
        {
            "content":    "",
            "subreddit":  "",
            "upvotes":    "",
            "timestamp":  "",
            "id":         "",
            "url":        "",
        },
    ],
    "discord": [
        {
            "content":
            "timestamp":
            "channel_id":
            "id":
            "url":
        }
    ],
    "twitter": [
        {
            "content":
            "timestamp":
            "likes":
            "replies":
            "retweets":
            "quote_tweets":
            "id":
            "url":
        }
    ]
}



'''


