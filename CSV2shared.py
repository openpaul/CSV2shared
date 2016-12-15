#/usr/bin/python
#python2
import sys
from pprint import pprint
class csv2shared():
    def __init__(self,infile, outfile, sep = '\t'):
        # defaults
        self.sep = sep
        self.label = "userLabel"
        self.Nfields = 0
        self.infile = infile

        # open in file
        
        # open Outfile
        self.fout = open(outfile, 'w')
       
        self.OTU = self.readFile()
        self.writeFile()
        #close file
        self.fin.close()
        
        
    def writeLine(self, line):
        self.fout.write('\t'.join(str(x) for x in line))
        self.fout.write('\n')
    
    def readFile(self):       
        OTU = []
        n = 0
        self.fin = open(self.infile, 'r')
        
            
            
        for line in self.fin:
            if  line[0:1] != '#': 

                #OTU.append([]) # init new list
                # split fields         
                fields = line.split(self.sep)
                
                #validate N Fields 
                if self.Nfields == 0:
                    self.Nfields = len(fields) 
                elif self.Nfields != len(fields):
                    print("Ahh field lenth does not match")
                
                OTU.append(fields)
                if n % 10 == 0: # print each 10
                    print('read line: ' + str(n) + " " + OTU[n][0])
                #pprint(fields)
                n = n + 1
        self.Nline = n
        self.fin.close()
        
        return OTU
        
    def writeFile(self):
        # write header:
        header = ['label','Group','numOtus']
        
        header = header + (self.returnColum(0)[1:])
        self.writeLine(header)
        print('Print header, done')
        i = 0
        
        # we dont just print each smaple
        # we sort them alphabetical to be more prettu
        s = map(str.strip, self.OTU[0])
        index = sorted(range(len(s)), key=lambda k: s[k])
  
        n = 0
        for i in index:
            if i != 0:
                col = [self.label, self.Nline - 1]
                col = col + self.returnColum(i)
                if n % 10 == 0: # print each 10
                    print('Processed sample called ' + str(col[2]))
                # switch 2 and 3 eg 1 and 2
                a       = col[1]
                b       = col[2]
                col[1]  = b
                col[2]  = a
                self.writeLine(col)
                n = n + 1
            
    
    def returnColum(self, n):
        col = []
        for line in self.OTU:
            col.append(line[n].strip())
        

        return col
            
          
        
print(sys.argv[1])
csv2shared(sys.argv[1], sys.argv[2])
