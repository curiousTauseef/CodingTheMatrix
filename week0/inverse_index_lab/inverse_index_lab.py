from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    dic_map = {}
    for x,y in enumerate(strlist):
        for word in y.split():
            if word in dic_map:
                dic_map[word] = dic_map[word] | {x}
            else:
                dic_map[word] = {x}
    return dic_map

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    any_doc = set()
    for word in query:
        if word in inverseIndex:
            any_doc = any_doc | inverseIndex[word]
    return any_doc

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    all_doc = set()
    first = True
    for word in query:
        if word in inverseIndex:
            if first is True:
                first = False
                all_doc = inverseIndex[word]
            else:
                all_doc = all_doc & inverseIndex[word]
    return all_doc
