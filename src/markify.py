# This is the start so that if only --version is given, it prints it out FAST

from VERSION  import VERSION
from argparse import ArgumentParser

def parse_the_fookin_args():
    parser = ArgumentParser(description='Markify is a command line application written in python which scrapes data from your social media(s) (ie reddit, discord, and twitter for now) and generates new setences based on them using markov chains. For more information, please visit https://github.com/msr8/markify')
    parser.add_argument('-c', '--config',  type=str,  help='The path to config file. By default, its {LOCALAPPDATA}/markify/config.json on windows, and ~/.config/markify/config.json on other operating systems')
    parser.add_argument('-d', '--data',    type=str,  help='The path to the json data file. If given, the program will not scrape any data and will just compile the model and generate sentences')
    parser.add_argument('-n', '--number',  type=int,  help='Number of sentences to generate. Default is 50', default=50)
    parser.add_argument('-v', '--version',            help='Print out the version number', action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_the_fookin_args()
    # If --version is given, prints the version and exits
    if args.version:    print(VERSION); exit()






# ------------------------------ IMPORTS ------------------------------
from main_funcs import init_config, do_reddit, do_discord, do_twitter, make_model, generate_sentences, print_stats
from util_funcs import get_user, get_config_dir

from colorama import init as color_init
from colorama import Fore, Style
from rich import print as printf
from rich.console import Console
from rich.panel import Panel

import platform as pf
import time as t











def main():
    color_init()
    # Gets the colors
    colors = {
        'res'  : Style.RESET_ALL,
        'res2' : Fore.RESET,
        'bol'  : Style.BRIGHT,
        'log'  : Style.BRIGHT + Fore.LIGHTGREEN_EX,
        'war'  : Style.BRIGHT + Fore.LIGHTYELLOW_EX,
        'err'  : Style.BRIGHT + Fore.LIGHTRED_EX,
        'spe'  : Fore.LIGHTMAGENTA_EX
    }
    res, log, spe = colors['res'], colors['log'], colors['spe']
    # Gets the args
    args = parse_the_fookin_args()
    # If --version is given, prints the version and exits
    if args.version:    print(VERSION); exit()
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
        do_twitter(CONFIG, DATA_FP, colors)
    # Makes the model
    model = make_model(DATA_FP, colors)
    # Generates the sentences
    generate_sentences(model, colors, args.number)
    # Prints the stats
    end = t.perf_counter()
    print_stats(DATA_FP, args.number, start, end, colors)
    








    
def init_main():
    console = Console()
    try:
        main()
    except Exception as e:
        panel = Panel(
            '[b i red]FATAL ERROR[/]',
            border_style = 'b'
        )
        printf('\n\n')
        printf(panel)
        printf('\n\n')
        console.print_exception()



if __name__ == '__main__':
    init_main()


























'''
BLUEPRINT


TODO
-> Improve time for argpare







3 files:
  main.py
  util_funcs.py
  main_funcs.py


The program:
  Config stuff
  Check cli input with the following params:
    number
    data
    config

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



