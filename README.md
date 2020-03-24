# Tiny Letter, Big Data
Statistics about your [tinyletter.com](https://tinyletter.com) newsletter, straight from the command line. Get quick summaries and dive into trends. Created mainly as a way to learn more about the many newsletters I send out, but feel free to use and contribute. 

If you do use this utility, please do right by your subscribers and let them know you are using this tool. If subscribers would like to opt out, you can support that by modifying the process_subscribers() function in [utils.py](https://github.com/anushadatar/TinyLetterBigData/blob/master/utils.py) to delete their row. 

## Usage

There are currently a few main commands built into [The TinyLetter CLI](https://github.com/anushadatar/TinyLetterBigData/blob/master/tinyletterbigdata.py). They can all be run from a standard command line interface.
- The update command:
```sh
python3 tlbd_cli.py -u
```
This command will create four csv files in your directory with cleaned and flattened data for subscribers, messages, drafts, and urls. These csv files can be processed independently or through the use of the following summary commands.

- The all-time statistics command:
```sh
python3 tlbd_cli.py -a
```
This command will report all-time statistics for the newsletter based on the most updated data by printing it to the console.
- The numbered issue statics command:
```sh
python3 tlbd_cli.py -i
```
This command will prompt the user to input which issue to get spcific data for and print that data to the console. 

## Installation and Dependencies
This program requires an installation of [Python 3](https://www.python.org/downloads/).

It also uses argparse, getpass, os, pandas, and tinyapi, which can all be installed via [pip](https://pypi.org/project/pip/). 

Then, clone this repository to get the code:
```sh
git clone https://github.com/anushadatar/TinyLetterBigData.git
```
