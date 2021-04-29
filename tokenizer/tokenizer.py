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
        code = code.replace('[',' [ ')
        code = code.replace(']',' ] ')
        _tokens = re.split(' ',code)
        tokens = []

        for i in range(0, len(_tokens)):
            t = _tokens[i]
    
            if t != "":
                #print("nouvelle ligne : ",t)
            
                #si le token est une classe
                if constantToken.typeClass in t:
                    tokens.append({"type": constantToken.typeClass,"value":t})# faire ca dans parser.py

                else:
                    #si le token est un main

                    ################################################################################################
                    res = {"type": "word", "value": t}
                    
                    if h.is_number_float(t) == False and t.isnumeric()==False:
                        res = {"type": "word", "value": t}

                    if t.isnumeric():
                        res = { "type" : "int", "value": int(t)}

                    if constantToken.typePrint == t:
                        res = {"type": constantToken.typePrint, "value": t}

                    if t in constantToken.JavaType:
                        res = {"type" : "JavaType", "value" : t}
        
                    if constantToken.symboleEqual == t:     
                            res = {"type": constantToken.symboleEqual, "value": t}
                    
                    if t in constantToken.typeVisibility:     
                            res = {"type": "visibility", "value": t}

                    if t == '}':
                        res = {"type" : constantToken.symboleCloseCurlyBracket, "value" : t}

                    if t == '{':
                        res ={"type" : constantToken.symboleOpenCurlyBracket, "value" : t}

                    if t == ')':
                        res = {"type" : constantToken.symboleCloseParenthese, "value" : t}

                    if t == '(':
                        res ={"type" : constantToken.symboleOpenParenthese, "value" : t}

                    if t == ']':
                        res = {"type" : constantToken.symboleCloseBracket, "value" : t}

                    if t == '[':
                        res ={"type" : constantToken.symboleOpenBracket, "value" : t}
                    
                    if "*" in t:
                        temp = t.replace("*", "")
                        if (temp in constantToken.specialChars):
                            res = {"type" : temp, "value" : constantToken.specialChars[temp]["value"]}

                    #################################################################################################
                    tokens.append(res)

        if len(tokens) < 1:
            raise Exception(constant.errorNoTokenFound)

        return tokens
