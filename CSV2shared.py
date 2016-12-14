#/usr/bin/python
#python2
import sys
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
        # get number of col
        rowNames = self.readColumn(0)
        del rowNames[3]
        self.writeLine(rowNames)
        
        # get column labes
        i = 0
        while i < self.Nfields:
            i = i + 1
            self.writeLine(self.readColumn(i))
        # loop each column transfer to row
        
        #close file
        self.fin.close()
    def writeLine(self, line):
        self.fout.write('\t'.join(str(x) for x in line))
        self.fout.write('\n')
    
    def readColumn(self, n):
        self.fin = open(self.infile, 'r')
        if n == 0:
            col = ['label','Group','numOtus']
        else:
            col = [self.label]
            
        firstLine = True
        for line in self.fin:
            fields = line.split(self.sep)
            if self.Nfields == 0:
                self.Nfields = len(fields) - 1
            elif self.Nfields != len(fields) -1:
                print("Ahh field lenth does not match")

            col.append(fields[n].strip())
            
            if firstLine == True and n != 0:
                col.append(self.Nfields)
            
                        
            firstLine = False
        self.fin.close()
        return col
        
        
print(sys.argv[1])
csv2shared(sys.argv[1], sys.argv[2])
