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
        while i < self.Nfields - 1:
            i = i + 1


            col = [self.label, self.Nline - 1]
            col = col + self.returnColum(i)
            print('Processed' + str(i) + ' called ' + str(col[2]))
            self.writeLine(col)
            
    
    def returnColum(self, n):
        col = []
        for line in self.OTU:
            col.append(line[n].strip())
        

        return col
            
          
        
print(sys.argv[1])
csv2shared(sys.argv[1], sys.argv[2])
