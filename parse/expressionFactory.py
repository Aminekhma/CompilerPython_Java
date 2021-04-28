from . import constantParser as consParser
from tokenizer import constantToken as consTokens
import sys 
sys.path.append('../tokenizer')

def create(type,tokens,start):
    if type == consParser.expressionClass:
        return classCreation(tokens, start)

    if type == consParser.expressionMethodCall:
        return objectMethodCall(tokens, start)

    if type == consParser.expressionDeclaration:
        return variableDeclaration(tokens, start)

    if type == consParser.expressionAffectation:
        return variableAffectation(tokens, start)

def objectMethodCall(tokens,start):
    objectName = tokens[start]["value"]
    if tokens[start+2]["type"] != consTokens.typeWord:
        return "error"
    methodName = tokens[start+2]["value"]
    arguments=helper.searchArgs(tokens,start+3)
    return {type:consParser.expressionMethodCall, objectName:objectName,methodName:methodName,arguments:arguments.args,end:arguments.end}

def variableDeclaration(tokens, start):
    #if tokens[start+1]["type"] != consTokens.typeWord: #cas erreur 
    #    print(tokens[start+1]["type"])
    #    return consParser.errorMissingWord
    variableName = tokens[start+1]["value"]
    return {type : consParser.expressionDeclaration, "variableName": variableName}

def variableAffectation(tokens, start):
    #if tokens[start-1]["type"] != consTokens.typeWord: #cas erreur
    #    return consParser.errorMissingWord
    #if tokens[start+1]["type"]==consTokens.typeNumber:
    #    variableValue = tokens[start+1]
    #else:
    #    if tokens[start+1]["type"]==consTokens.symboleQuotationMark:
    #        variableValue= helper.searchString(tokens, start+1)
    return {type: consParser.expressionAffectation, "variableName": tokens[start-2]["value"], "variableValue": tokens[start+1]["value"]}


def classCreation(tokens, start):
    return {"type": consParser.expressionClass, "className": tokens[start+1]["value"], "classType": tokens[start-1]["value"] , "bodyclass" : [] }



