from tokenizer import tokenizer
from tokenizer import helper
from parse import parse
from scoring import scoring

import re

#file = open("Test.java","r")
    
with open('Test.java') as file:
    score = scoring.Scoring()
    s = score.scoring(file.read())

    print(s)
    #token = tokenizer.Token()
    #tokens = token.tokenizer(file.read())
    #parsers = parse.Parser()
    #ast = parsers.readTokens(tokens)

 
