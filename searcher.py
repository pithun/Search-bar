"""So i got tired of opening all my files one by one to search for things i need to refer to. So with this code
i basically opened all my files, did the necessary cleaning and i made my very own search bar."""

import pandas as pd
import os
import re

# getting access to the files in the directory

wd = os.getcwd()
raw_files = os.listdir(wd)
my_files = []

# Using the regular expressions to find just csv, py and txt files to be read.
pattern = re.compile(r'.*\.(csv|py|txt)')

for x in raw_files:
    matches = pattern.finditer(x)
    for match in matches:
        my_files.append(match.group(0))

print(my_files)


def search_bar(files, keyword):
    for f in files:
        """Opening and reading my files"""
        content = []
        viewing = open(f, 'r')
        reading_viewing = viewing.read()
        """changing to lower case and cleaning"""
        spliting_words = str(reading_viewing).lower().split()
        for a_word in spliting_words:
            symb = "!£$%^*()+-={}~[]#:@;'<>?,/\""
            for a in range(len(symb)):
                a_word = a_word.replace(symb[a], '')
            if len(a_word) > 0:
                content.append(a_word)

        """passing into a dataframe and using the .str.contains to filter words"""
        ref = {str(f): content}
        refdf = pd.DataFrame(ref)
        # conditions = len(refdf.values)
        # print(conditions)
        """making sure i don't print out an empty dataframe"""
        what_i_want = refdf[refdf[str(f)].str.contains(keyword)]
        if len(what_i_want) > 0:
            print(what_i_want, '\n')
        else:
            pass


search_bar(my_files, 'alchemy')

# MISSION ACCOMPLISHED.
