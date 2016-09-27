#!/usr/bin/env python

"""
A filter that removes stop words from input.
"""

import fileinput

# List of stop words taken from http://www.ranks.nl/stopwords
stop = ['a','about','above','after','again','against','all','am','an','and','any','are','aren','as','at','be','because','been','before','being','below','between','both','but','by','can','cannot','could','couldn','d','did','didn','do','does','doesn','doing','don','down','during','each','few','for','from','further','had','hadn','has','hasn','have','haven','having','he','her','here','hers','herself','him','himself','his','how','i','if','in','into','is','isn','it','its','itself','ll','let','m','me','more','most','mustn','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own','s','same','shan','she','should','shouldn','so','some','such','t','than','that','the','their','theirs','them','themselves','then','there','there','these','they','this','those','through','to','too','under','until','up','ve','very','was','wasn','we','were','weren','what','when','where','which','while','who','whom','why','with','won','would','wouldn','you','your','yours','yourself','yourselves']


def filter(word):
    """Remove stop words from list"""
    if word.strip() not in stop: # Print word only if it is not a stop word
        print(word.strip())


for word in fileinput.input():
    filter(word)
