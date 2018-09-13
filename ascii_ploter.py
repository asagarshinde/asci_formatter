import math
output = {100: 12911074, 200: 3125360, 600: 2204013, 500: 2107324, 400: 1615420, 300: 1287883, 700: 67207, 0: 47}

class Formatter(object):
    def __init__(self,inp,col1_header='key',col2_header='values'):
        self.inp = inp
        self.x = 0
        self.y = 0
        self.col1_header = col1_header
        self.col2_header = col2_header
        
    def max_len(self):
        li = self.inp.values() + self.inp.keys()
        self.x = max([len(str(x)) for x in self.inp.keys()])
        self.y = max([len(str(x)) for x in self.inp.values()])
     
    def display(self):
        self.max_len()
        print '-'*(self.x + self.y+ 7)
        print "| {:{}} | {:{}} |".format(self.col1_header,self.x,self.col2_header,self.y)
        print '-'*(self.x + self.y + 7)
        for k,v in self.inp.items():
            print "| {:{}} | {:{}} |".format(k,self.x,v,self.y)


formatter = Formatter(output)
formatter.display()

