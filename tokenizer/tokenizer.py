from . import helper
from . import constantToken
import re

class Token :

    def tokenizer(self,c):
        #line = re.split('}|{',l)
        h = helper.Helper()

        code = h.replaceSpecialsChars(c)
        code = code.replace('}',' } ')
        code = code.replace('{',' { ')
        code = code.replace('(',' ( ')
        code = code.replace(')',' ) ')
        _tokens = re.split(' ',code)
        tokens = []

        for i in range(0, len(_tokens)):
            t = _tokens[i]

            
            if t != "":
                print("nouvelle ligne : ",t)
            
                #si le token est une classe
                if constantToken.typeClass in t:
                    tokens.append({"type": constantToken.typeClass,"value":t})# faire ca dans parser.py

                else:
                    #si le token est un main

                    #################################################################################################

                    tokens.append({"type": "inconnu", "value": t})

                    if constantToken.typeClass == t:
                            tokens.append({"type": constantToken.typePrint, "value": t})

                    if constantToken.typeWord == t:
                            tokens.append({"type": constantToken.typeWord, "value": t})

                    if constantToken.typeNumber == t:     
                            tokens.append({"type": constantToken.typeNumber, "value": t})
        
                    if constantToken.symboleEqual == t:     
                            tokens.append({"type": constantToken.symboleEqual, "value": t})
                    
                    #################################################################################################


        if len(tokens) < 1:
            raise Exception(constant.errorNoTokenFound)

        return tokens
