# Introduction

Markovify is a command line application written in python which scrapes data from your social media(s) (ie reddit, discord, and twitter for now) and generates new setences based on them using markov chains

<br>

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

<br>

# Usage

To use, you can simply just run `markify` on the command line, but we gotta setup a config file first. If you're windows, the default location for the config file is `%LOCALAPPDATA%\markify\config.json`, and on linux/macOS it is `~/.config/markify/config.json`. Alterantivly, you can provide the path to the config file using the `-c --config` flag. An ideal config file should look like:
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

<br>

# Flags

You can view the available flags by running `markify --help`. It should show the following text:
```
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        The path to config file. By default, its {LOCALAPPDATA}/markone/config.json
                        on windows, and ~/.config/markone/config.json on other operating systems
  -d DATA, --data DATA  The path to the json data file. If given, the program will not scrape any
                        data and will just compile the model and generate sentences
  -n NUMBER, --number NUMBER
                        Number of sentences to generate. Default is 50
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




