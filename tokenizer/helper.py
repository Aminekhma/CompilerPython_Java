from . import constantToken

class Helper :

    def __init__(self):
        self.liste = []

    '''def replaceSpecialsChars(self, c):
        for i in self.liste :
            if self.detectTabulation(i):
                print(i)'''
    #permet de mettre sous forme de liste chaque ligne du fichier (je sais pas si ca va servir)
    '''def parserLine(self,code):
        res = ""
        for i in code:
            if(i=="\n"):
                self.liste.append(res)
                res = ""
            else:
                res = res + i
        self.liste.append(res)
        return code'''

    #permet de savoir si une ligne possede une tabulation ()
    '''def detectTabulation(self,line):
        res = 0
        for i in line :
            if i != " ":
                return False
            res+=1
        if res % 4 == 0 :
            return True'''

    def checkChars(self,t):
        for charName in constantToken.specialChars :
            if(t=='*'+charName+'*'):
                return charName
        return False

    def replaceSpecialsChars(self,code):
        for charName in constantToken.specialChars:
            element = constantToken.specialChars[charName]
            code = code.replace(element['value'], ' *'+charName+'* ')
        return code

    """def splitter(self,code):
        for line in code:
            line.replace("\t","TEST")
            print(line)
            print("----------")"""
    
    def is_number_float(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False