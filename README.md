<!--
COLORS:

302D41 (label)
96CDFB (blue)
DDB6F2 (pink)
ABE9B3 (green)
F8BD96 (orange)
-->

<br>

<div align='center'>

   <!-- <img src="https://img.shields.io/github/stars/msr8/markify?color=FFBE0B&labelColor=302D41&style=for-the-badge">
   <img src="https://img.shields.io/pypi/v/markify?color=FB5607&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/github/last-commit/msr8/markify?color=FF006E&labelColor=302D41&style=for-the-badge">   
   <img src="https://img.shields.io/github/issues/msr8/markify?color=8338EC&labelColor=302D41&style=for-the-badge">
   <img src="https://img.shields.io/github/license/msr8/markify?color=3A86FF&labelColor=302D41&style=for-the-badge"/>

   <br><br><br> -->

   <img src="https://img.shields.io/github/stars/msr8/markify?color=F72585&labelColor=302D41&style=for-the-badge">
   <img src="https://img.shields.io/pypi/v/markify?color=7209B7&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/github/last-commit/msr8/markify?color=3A0CA3&labelColor=302D41&style=for-the-badge">   
   <img src="https://img.shields.io/github/issues/msr8/markify?color=4361EE&labelColor=302D41&style=for-the-badge">
   <img src="https://img.shields.io/github/license/msr8/markify?color=4CC9F0&labelColor=302D41&style=for-the-badge"/>

   <!-- <br><br><br>

   <img src="https://img.shields.io/github/stars/msr8/markify?color=CDB4DB&labelColor=302D41&style=for-the-badge">
   <img src="https://img.shields.io/pypi/v/markify?color=FFC8DD&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/github/last-commit/msr8/markify?color=FFAFCC&labelColor=302D41&style=for-the-badge">   
   <img src="https://img.shields.io/github/issues/msr8/markify?color=BDE0FE&labelColor=302D41&style=for-the-badge">
   <img src="https://img.shields.io/github/license/msr8/markify?color=A2D2FF&labelColor=302D41&style=for-the-badge"/> -->

   <!-- <br><br><br>

   <img src="https://img.shields.io/github/stars/msr8/markify?color=F8BD96&labelColor=302D41&style=for-the-badge">
   <img src="https://img.shields.io/pypi/v/markify?color=048A81&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/github/last-commit/msr8/markify?color=DDB6F2&labelColor=302D41&style=for-the-badge">   
   <img src="https://img.shields.io/github/issues/msr8/markify?color=ABE9B3&labelColor=302D41&style=for-the-badge">   
   <img src="https://img.shields.io/github/license/msr8/markify?color=96CDFB&labelColor=302D41&style=for-the-badge"/> -->

   <!-- <br><br>
   <img src="https://img.shields.io/pypi/v/markify?color=69626D&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/pypi/v/markify?color=AB4E68&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/pypi/v/markify?color=305252&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/pypi/v/markify?color=E36588&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/pypi/v/markify?color=545454&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/pypi/v/markify?color=048A81&labelColor=302D41&style=for-the-badge"/>
   <img src="https://img.shields.io/pypi/v/markify?color=9D6381&labelColor=302D41&style=for-the-badge"/> -->

   <br>

   <!-- <video controls> 
        <source src='https://raw.githubusercontent.com/msr8/markify/main/ass/usagelol.mp4' type="video/mp4">lol
    </video> -->
</div>

<br>

https://user-images.githubusercontent.com/79649185/182558272-255becc8-1dcc-45b5-99ef-22e0596cf490.mp4

<!-- <br> -->

<p align='center'>
<a href='https://github.com/msr8/markify' >Github</a> |
<a href='https://pypi.org/project/markify'>PyPi</a>
</p>








# Index

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Flags](#flags)
* [How does this work?](#how-does-this-work)
* [FAQs](#faqs)

<br><br>
<br><br>

# Introduction

Markify is an open source command line application written in python which scrapes data from your social media(s) (ie reddit, discord, and twitter for now) and generates new setences based on them using markov chains

<br><br>

# Installation

There are many methods to install markify on your device, such as:

<br>

## 1) Install the pip package
***(Reccomended)***

```bash
python -m pip install markify
```

## 2) Install it via pip and git

```bash
python -m pip install git+https://github.com/msr8/markify.git
```

## 3) Clone the repo and install the package

```bash
git clone https://github.com/msr8/markify
cd markify
python setup.py install
```

## 4) Clone the repo and run markify without installing to PATH

```bash
git clone https://github.com/msr8/markify
cd markify
python -m pip install -r requirements.txt
cd src
python markify.py
```

<br><br>

# Usage

To use, you can simply just run `markify` on the command line, but we gotta setup a config file first. If you're windows, the default location for the config file is `%LOCALAPPDATA%\markify\config.json`, and on linux/macOS it is `~/.config/markify/config.json`. Alterantively, you can provide the path to the config file using the `-c --config` flag. If you run the program and the config file doesn't exist, it makes an empty template. An ideal config file should look like:
```json
{
    "reddit": {
        "username"     : "..."
    },
    "discord": {
        "token"        : "..."
    },
    "twitter": {
        "username"     : "..."
    }
}
```
where the username under reddit section is your reddit username, token under discord is your discord token, and username under twitter is your twitter username. If any of them are not given, the program will skip the collection process for that social media

<br><br>

# Flags

You can view the available flags by running `markify --help`. It should show the following text:
```
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        The path to config file. By default, its {LOCALAPPDATA}/markify/config.json on
                        windows, and ~/.config/markify/config.json on other operating systems
  -d DATA, --data DATA  The path to the json data file. If given, the program will not scrape any data and
                        will just compile the model and generate sentences
  -n NUMBER, --number NUMBER
                        Number of sentences to generate. Default is 50
  -v, --version         Print out the version number
```
More explanation is given below:

<br>

## -c --config

This is the path to the config file (config.json). By default, its `{LOCALAPPDATA}/markify/config.json` on windows, and `~/.config/markify/config.json` on other operating systems. For example:
```bash
markify -c /Users/tyrell/Documents/config.json
```

## -d --data

This is the path to the data file containing all the scraped content. If it is given, the program doesn't scrape any data and just complies a model based on the data present in the file. By default, a new data file is generated in the `DATA` folder in the config folder and is named `x.json` where `x` is the current epoch time in seconds. For example:
```bash
markify -d /Users/tyrell/.config/markify/DATA/1658433988.json
```

## -n --number

This is the number of sentences to generate after compiling the model. Default is 50. For example:
```bash
markify -n 20
```

## -v --version

Print out the version of markify you're using via this flag. For example:
```bash
markify -v
```

<br><br>

# How does this work?

This program has 4 main parts: Scraping reddit comments, scraping discord messages, scraping tweets, generating sentences using markov chains. More explanation is given below

<br>

## Scraping reddit comments

The program uses the [Pushshift's API](https://github.com/pushshift/api) to scrape your comments. Since Pushshift can only return 100 comments at a time, the program gets the timestamp of the oldest comment and then sends a request to the API to get comments before that timestamp. This loop goes on until either all your comments are scraped, or 10000 comments are scraped. I chose to use Pushshift's API since its faster, yeilds more result, and doesnt need a client ID or secret

<br>

## Scraping discord messages

To scrape discord messages, first the program checks if the token is valid or not by getting basic information (username, discriminator, and account ID) through the `/users/@me` endpoint. Then it gets all the DM channels you have participated in through the `/@me/channels` endpoint. Then it extracts the channel IDs from the response and gets the recent 100 messages in the channels using the `/channels/channelid/messages` endpoint, where `channelid` is the channel ID. Then it goes through the respone and adds the messages which are a text message, sent by you, and arent empty, to the data file

<br>

## Scraping tweets

The program uses the [snscrape](https://github.com/JustAnotherArchivist/snscrape) module to scrape your tweets. The program keeps scraping your tweets until either it has scraped all the tweets, or has scraped 10000 tweets

<br>

## Generating sentences using markov chains

The program extracts all the useful texts from the data file and makes a markov chain model based on them using the [markovify](https://github.com/jsvine/markovify) module. Then the program generates new sentences (default being 50) and prints them out

<br><br>

# FAQs

<br>

### Q) How do I get my discord token?

Recently (as of July 2022), discord reworked its system of tokens and the format of the new tokes is a bit different. You can obtain your discord token using this [guide](https://www.androidauthority.com/get-discord-token-3149920/)

<br>

### Q) The program is throwing an error and is telling me to install "averaged_perceptron_tagger" or something. What to do?

Running the command given below should work
```bash
python3 -c "import nltk; nltk.download('averaged_perceptron_tagger')"
```
You can visit [this page](https://www.nltk.org/data.html) for more information

<br>

### Q) The installation is stuck at building lxml. What to do?

Sadly, all you can do is wait. It is a [known issue with lxml](https://stackoverflow.com/questions/33064433/lxml-will-never-finish-building-on-ubuntu)











<!-- 
TODO

-> Convert the video to a video tag in setup.py
-->




