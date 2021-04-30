import sys 
sys.path.append('../tokenizer')
from tokenizer import tokenizer
from parse import parse
from . import helper
import re


class Scoring:

    def scoring(self, code):
        print("")
        print("----------","Tokens","----------")
        token = tokenizer.Token()
        tokens = token.tokenizer(code)
        print(tokens)
        print("")


        print("-----------","AST","-----------")
        parser = parse.Parser()
        ast = parser.readTokens(tokens)
        print(ast)
        print("")


        h = helper.Helper()

        resultat = { "allDeclaredIsUsed" : h.allDeclaredIsUsed(ast),
            "allUsedIsDeclared" : h.allUsedIsDeclared(ast),
            "allExpressionFinished": h.allExpressionFinished(ast),
            "numberLine": h.numberLine(code),
            "indentation": h.indentation(code)}

        return  {"score" : resultat["allDeclaredIsUsed"]+ 
                            resultat["allUsedIsDeclared"]+ 
                            resultat["allExpressionFinished"]+ 
                            resultat["numberLine"]+ 
                            resultat["indentation"]}

