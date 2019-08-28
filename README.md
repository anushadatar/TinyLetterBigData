# Tiny Letter, Big Data
Statistics about your [tinyletter.com](https://tinyletter.com) newsletter, straight from the command line. Get quick summaries and dive into trends. Created mainly as a way to learn more about the many newsletters I send out, but feel free to use and contribute. 

## Usage

There are currently a few main commands built into [tinyletterbigdata.py](https://github.com/anushadatar/TinyLetterBigData/blob/master/tinyletterbigdata.py). They can all be run from a standard command line interface.
- The update command:
```sh
python3 tinyletter.py -u
```
This command will create four csv files in your directory with cleaned and flattened data for subscribers, messages, drafts, and urls. These csv files can be processed independently or through the use of the following summary commands.

- The all-time statistics command:
```sh
python3 tinyletter.py -a
```
This command will report all-time statistics for the newsletter based on the most updated data by printing it to the console.
- The numbered issue statics command:
```sh
python3 tinyletter.py -i
```
This command will prompt the user to input which issue to get spcific data for and print that data to the console. 

## Installation and Dependencies
This program requires an installation of [Python 3](https://www.python.org/downloads/).

It also uses argparse, getpass, os, pandas, and tinyapi, which can all be installed via [pip](https://pypi.org/project/pip/). 

Then, clone this repository to get the code:
```sh
git clone https://github.com/anushadatar/TinyLetterBigData.git
```
