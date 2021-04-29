from tokenizer import tokenizer
from tokenizer import helper
from parse import parse
import re

#file = open("Test.java","r")
    
with open('Test.java') as file:
    token = tokenizer.Token()
    tokens = token.tokenizer(file.read())
    print(tokens)
    parsers = parse.Parser()
    #print(parsers.readTokens(tokens))