import constantParser as constParser
import sys 

sys.path.append('../tokenizer')

import constantToken as constTokens

class helper:

    def searchString(self, tokens, start):
        string = []
        findend = false
        end = None
        
        for i in range (0, len(tokens)):
            if token[i]["type"] == constTokens.symboleQuotationMark: 
                findend = true
                end = i
                break
            else:
                string.append(token[i]["value"])

        if(not findend):
            raise consParser.errorMissingQuotationMark

        return {type:constParser.typeString, value: string.join(' '), start: start, end: end}


    def searchArgument(self, tokens, start):
        if tokens[start].type != constTokens.symboleOpenParenthese:
            raise constParser.errorMissingOpenParenthesis
        
        findEnd = False
        end = None
        args = []

        for i in range(0, len(tokens)):
            if tokens[i].type==constTokens.symboleCloseParenthese:
                findEnd= true
                end=i
                break
            else:
                if(tokens[i].type==constTokens.typeWord):
                    args.append({type:constParser.typeVariable, variableName:tokens[i]["value"]})
                else:
                    if tokens[i].type==constTokens.typeNumber:
                        args.append(tokens[i])
                    else :
                        if tokens[i].type==constTokens.symboleQuotationMark :
                            temp = searchString(tokens, i)
                            args.append(temp)
                            i=temp.end
        if not findEnd: 
            raise constParser.errorMissingCloseParenthesis
        
        return {args: args, end: end}

    def searchBody(self, tokens, start):
        if tokens[start]["type"] != constTokens.symboleOpenCurlyBracket:
            raise constParser.errorMissingOpenBracket
        findEnd = False
        end = None
        body = []
        for i in range(0, len(tokens)):
            if tokens[i]["type"]==constTokens.symboleCloseCurlyBracket:
                findEnd= true
                end=i
                break
            else:
                if(tokens[i]["type"]==constTokens.typeWord):
                    args.append({type:constParser.typeVariable, variableName:tokens[i]["value"]})
                else:
                    if tokens[i].type==constTokens.typeNumber:
                        args.append(tokens[i])
                    else :
                        if tokens[i]["type"]==constTokens.symboleQuotationMark :
                            temp = searchString(tokens, i)
                            args.append(temp)
                            i=temp.end
        if not findEnd: 
            raise constParser.errorMissingCloseParenthesis
        
        return {body: body, end: end}


