import sys 
sys.path.append('../tokenizer')
sys.path.append('../parser')
from parse import constantParser as consParser

class Helper:

    def allDeclaredIsUsed(self, ast):
        cpt1=0
        cpt2=0
        var=""
        for i1 in ast:
            if i1["type"] == "class":
                for i2 in i1["bodyclass"]:
                    if i2["type"] == "main":
                        for i3 in i2["bodyMain"]:
                            if i3["type"] == "variableDeclaration":
                                cpt1 = cpt1 + 1
                                var = i3["variableName"]
                            if i3["type"] == "variableAffectation" and i3["variableName"] == var:
                                cpt2 = cpt2 + 1

        if cpt1 == cpt2:
            return 1
        else:
            return 0 

    def allUsedIsDeclared(self, ast):
        cpt1=0
        cpt2=0
        var=""
        nb_affectation=0
        for i1 in ast:
            if i1["type"] == "class":
                for i2 in i1["bodyclass"]:
                    if i2["type"] == "main":
                        for i3 in i2["bodyMain"]:
                            if i3["type"] == "variableAffectation":
                                nb_affectation+=1
                            if i3["type"] == "variableDeclaration":
                                var = i3["variableName"]
                            if i3["type"] == "variableAffectation" and i3["variableName"] == var:
                                cpt2 = cpt2 + 1
                    else:
                        if i3["type"] == "variableAffectation":
                            nb_affectation+=1
                        if i3["type"] == "variableDeclaration":
                            var = i3["variableName"]
                        if i3["type"] == "variableAffectation" and i3["variableName"] == var:
                            cpt2 = cpt2 + 1
            else:
                if i3["type"] == "variableAffectation":
                    nb_affectation+=1
                    if i3["type"] == "variableDeclaration":
                        var = i3["variableName"]
                    if i3["type"] == "variableAffectation" and i3["variableName"] == var:
                        cpt2 = cpt2 + 1

        if nb_affectation == cpt2:
            return 1
        else:
            return 0 


    def allExpressionFinished(self, ast):
        expressionError = False

        for i1 in ast:
            if i1["type"] == "class":
                for i2 in i1["bodyclass"]:
                    if i2["type"] == "main":
                        for i3 in i2["bodyMain"]:
                            if i3 == consParser.errorMissingOpenParenthesis:
                                expressionError = True
                            if i3 == consParser.errorMissingCloseParenthesis:
                                expressionError = True
                            if i3 == consParser.errorMissingQuotationMark:
                                expressionError = True
                            if i3 == consParser.errorMissingWord:
                                expressionError = True
                            if i3 == consParser.errorMissingOpenBracket:
                                expressionError = True
                            if i3 == consParser.errorMissingCloseBracket:
                                expressionError = True
                    else:
                        if i3 == consParser.errorMissingOpenParenthesis:
                            expressionError = True
                        if i3 == consParser.errorMissingCloseParenthesis:
                            expressionError = True
                        if i3 == consParser.errorMissingQuotationMark:
                            expressionError = True
                        if i3 == consParser.errorMissingWord:
                            expressionError = True
                        if i3 == consParser.errorMissingOpenBracket:
                            expressionError = True
                        if i3 == consParser.errorMissingCloseBracket:
                            expressionError = True

            else:
                if i3 == consParser.errorMissingOpenParenthesis:
                    expressionError = True
                if i3 == consParser.errorMissingCloseParenthesis:
                    expressionError = True
                if i3 == consParser.errorMissingQuotationMark:
                    expressionError = True
                if i3 == consParser.errorMissingWord:
                    expressionError = True
                if i3 == consParser.errorMissingOpenBracket:
                    expressionError = True
                if i3 == consParser.errorMissingCloseBracket:
                    expressionError = True

        if expressionError == False:
            return 1
        else:
            return 0 


    def indentation(self, code):
        with open("Test.java") as file:
            text=file.read()
            count_tab=0
            count_space=0
            count_newline=0
            for char in text:
                if char=='':
                    count_tab+=1
                if char==' ':
                    count_space+=1
                if char=='\n':
                    count_newline+=1
        
        #print("How many Tabs are present in these file? ", count_tab)

        return 0


    def numberLine(self, code):
        
        cpt = 0
        for line in code:
            if line == "\n":   
                cpt+=1
        if cpt >200:   
            return 0
        else:
            return 1
