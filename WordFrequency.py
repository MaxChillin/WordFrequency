"""
Author: Jeremy Pierce
Date: 9/5/18

Instructions:

1.	In a for loop, 
    (a) read in each file, 
    (b) use the string.replace() method to replace newlines with spaces, 
    (c) use the string.lower() method to lower case the text, then use NLTK tokenizer to extract tokens, 
    (d) make a FreqDist from the tokens, 
    (3) print the filename and 5 most common words, 
    (e) on each iteration through the files, add the FreqDist to a cumulative FreqDist for later.

2.	Repeat the same loop as above but add the following: 
    (a) remove punctuation symbols before tokenizing, 
    (b) remove stopwords.

3.	For your cumulative FreqDist for steps 2 and 3, create a cumulative frequency graph of the 50 most 
    common words. Note that you may have to install matplotlib, and the first time matplotlib runs it 
    takes a while. 

"""

import os
import sys
import nltk
from nltk.probability import FreqDist
from nltk import word_tokenize
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import re
import matplotlib

def main():
    # This is for part 3
    cumulativeDist = FreqDist()
    
    # Print an appropriate error message if the sys.argv is missing and end the program
    if len(sys.argv) < 2:
        return print("Error: Missing System Argument(s)!")
    else:
        # Within your main() function, get the directory name from a system argument
        for filename in os.listdir(sys.argv[1]):
            
            # 1(a) read in each file
            if filename.endswith('.txt'):
                with open (sys.argv[1]+filename, 'r') as f:
                    text = f.read()

                    # 1(b) use the string.replace() method to replace newlines with spaces
                    text.replace("\n", " ")

                    # 1(c) use the string.lower() method to lower case the text, 
                    # then use NLTK tokenizer to extract tokens
                    text.lower()
                    tokens = word_tokenize(text)

                    # 1(d) make a FreqDist from the tokens
                    currentDist = FreqDist(tokens)

                    # 1(3) print the filename and 5 most common words
                    print("\nFile name:",filename, "\n5 most common words:", currentDist.most_common(5))

                    # 1(e) on each iteration through the files, 
                    # add the FreqDist to a cumulative FreqDist for later
                    cumulativeDist += currentDist

        print()

        # 2.Repeat the same loop as above but add the following: 
        for filename in os.listdir(sys.argv[1]):
            if filename.endswith('.txt'):
                with open (sys.argv[1]+filename, 'r') as f:
                    text = f.read()
                    
                    # 2(a) remove punctuation symbols before tokenizing
                    text = re.sub(r'[.?!,:;``\"\'()\-\n\d]',' ', text.lower())
                    tokens = word_tokenize(text)

                    
                    # 2(b) remove stopwords.
                    stop_words = set(stopwords.words('english'))
                    tokens = [t for t in tokens if not t in stop_words]
                    currentDist = FreqDist(tokens)
                    print("\nFile name:",filename, "\n5 most common words:", currentDist.most_common(5))

    # 3) create a cumulative frequency graph of the 50 most common words
    cumulativeDist.plot(50, cumulative = True)

if __name__ == '__main__':
    main()