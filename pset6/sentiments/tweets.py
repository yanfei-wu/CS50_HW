#!/usr/bin/env python3

import os
import sys

from analyzer import Analyzer
from helpers import get_user_timeline
from termcolor import colored


def main():

    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: ./smile @username")

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)
    
    # get latest 50 tweets of the user
    tweets = get_user_timeline(sys.argv[1].strip('@'), count=50)
    if tweets == None:
        sys.exit("User doesn't exist or is private")
        
    # analyze tweets
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        if score > 0.0:
            print(colored(tweet, "green"))
        elif score < 0.0:
            print(colored(tweet, "red"))
        else:
            print(colored(tweet, "yellow"))

if __name__ == "__main__":
    main()
