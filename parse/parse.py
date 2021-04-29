from parse import constantParser as constParser
import sys 
sys.path.append('../tokenizer')
from tokenizer import constantToken as constTokens
from . import expressionFactory as factory

class Parser:

    def readTokens(self, tokens):
        AST= []
        classe = False
        
        for i in range(0, len(tokens)):
            expression = None

            if tokens[i]["type"] == constTokens.typeWord:
                expression= factory.create(constParser.expressionDeclaration, tokens, i)
                i = i+1

            elif tokens[i]["type"] == constTokens.typeClass:
                expression= factory.create(constParser.expressionClass, tokens, i)
                i = i+1
                
            elif tokens[i]["type"] == constTokens.typeNumber:
                expression= factory.create(constParser.expressionDeclaration, tokens, i)
                i = i+1

            elif tokens[i]["type"] == constTokens.symboleEqual:
                expression = factory.create(constParser.expressionAffectation, tokens, i)
                #if expression.variableValue.type == constTokens.typeNumber:
                i = i+1

                #else:
                 #   i = expression.variableValue.end
            elif i<len(tokens)-1 and tokens[i]["type"] == constTokens.typeWord and tokens[i+1]["type"]==constTokens.symbolePoint :
                expression = factory.create(constParser.expressionMethodCall, tokens, i)
                i= expression.end
                
            if expression:
                if len(AST)>0 and classe==False:
                    for i in range(0,len(AST)):
                        if AST[i]["type"] == "class":
                            classe=True
                            classpos=i
                if classe == True:
                    AST[classpos]["bodyclass"].append(expression)

                AST.append(expression)
                
        return AST