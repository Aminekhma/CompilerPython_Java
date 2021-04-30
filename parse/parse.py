from parse import constantParser as constParser
import sys 
sys.path.append('../tokenizer')
from tokenizer import constantToken as constTokens
from . import expressionFactory as factory

class Parser:

    def readTokens(self, tokens):
        AST= []
        classe = False
        main = False
        i = 0
        

        while i < len(tokens):
            expression = None

            if tokens[i]["type"] == constTokens.typeString and tokens[i+1]["type"] != constTokens.symboleOpenBracket:                
                expression= factory.create(constParser.expressionDeclaration, tokens, i)
            
            elif tokens[i]["type"] == constTokens.typeMain:
                expression= factory.create(constParser.typeMain, tokens, i)

            elif tokens[i]["type"] == constTokens.typeClass:
                expression= factory.create(constParser.expressionClass, tokens, i)
                i = i

            elif tokens[i]["type"] == constTokens.typeNumber and tokens[i+1]["type"] != "int":
                expression= factory.create(constParser.expressionDeclaration, tokens, i)

            elif tokens[i]["type"] == constTokens.symboleEqual and (tokens[i+1]["type"] == "int" or tokens[i+1]["type"] != constTokens.typeWord ) :
                expression = factory.create(constParser.expressionAffectation, tokens, i)

            i = i + 1
            j = 0
            x=0
            classpos=0
    
            if expression:
                if len(AST)>0 and classe==False :
                    for j in range(0,len(AST)):
                        if AST[j]["type"] == "class":
                            classe=True
                            classpos=j

                if len(AST)>0 and main==False and classe == True:
                    dic = AST[classpos]["bodyclass"]
                    for x in range(0,len(dic)):
                        dic = AST[classpos]["bodyclass"]
                        if dic[x]["type"] == "main":
                            main=True
                            mainpos=x

                if classe == True and main == False:
                    AST[classpos]["bodyclass"].append(expression)
                elif main == True:
                    (AST[classpos]["bodyclass"])[mainpos]["bodyMain"].append(expression)
                else:
                    AST.append(expression)
                
        return AST