#!/usr/bin/python

# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA


# use this to transform any abundance table, such as an OTU table
# into a .shared file, as used by Mothur (https://www.mothur.org/)
# 
# call via
# python CSV2shared.py input.csv output.shared
# the seperator is declared in the script and may be changed here:

sep = '\t'
#sep = ','

import sys
from pprint import pprint
class csv2shared():
    def __init__(self,infile, outfile, sep = '\t'):
        # seome inti variables
        self.sep        = sep
        self.label      = "userLabel"
        self.Nfields    = 0
        self.infile     = infile
        self.outfile    = outfile
        
        
        
        # read the input file now
        self.OTU    = self.readFile()
        
        # transform the file while writing       
        self.writeFile()
        
        print("All done")
        
        
        
    def writeLine(self, line):
        '''
            takes a list as joins it to write it
        '''
        self.fout.write('\t'.join(str(x) for x in line))
        self.fout.write('\n')
    
    def readFile(self):      
        '''
        Opens the CSV table and reads it all into memory
        ''' 
        OTU         = []
        n           = 0 # step counter
        self.fin    = open(self.infile, 'r')
        
        # loop the lines
        for line in self.fin:
            if  line[0:1] != '#':  # exclude comments

                # split fields         
                fields = line.split(self.sep)
                
                #validate number of fields as a sanity check
                if self.Nfields == 0:
                    self.Nfields = len(fields) 
                elif self.Nfields != len(fields):
                    print("Warning: field length does not match. Check your seperator!")
                
                # save fields
                OTU.append(fields)
                
                if n % 100 == 0: # print each 100, so we know that it is working
                    print('currently read line: ' + str(n) + " " + OTU[n][0])
                
                n = n + 1 # raise step counter
                
        self.Nline = n # important to keep track of, as this is a required field by .shared
        self.fin.close()
        
        return OTU
        
    def writeFile(self):
        '''
        Take the OTU and write each colum in an line
        With some additional columns and such
        '''
        
        self.fout   = open(self.outfile, 'w')
        
        # write header:
        header = ['label','Group','numOtus']
        header = header + (self.returnColum(0)[1:])
        self.writeLine(header)
        print('Print header, done')
        
        
        # we dont just print each smaple
        # we sort them alphabetical to be more pretty
        s = map(str.strip, self.OTU[0])
        index = sorted(range(len(s)), key=lambda k: s[k])
  
        n = 0 # debug counter
        for i in index:
            if i != 0: # skip first column
                # init the colum which will become a row
                col     = [self.label, self.Nline - 1]
                col     = col + self.returnColum(i)
                
          
                # need to make a swap here, as this is the most
                # simple way I could think of dooing this
                a       = col[1]
                col[1]  = col[2]
                col[2]  = a
                # write the line
                self.writeLine(col)
                
                if n % 100 == 0: # print each 10
                    print('Processed sample called ' + str(col[1]))
                    
                
                n = n + 1 # step counter raise
        
        self.fout.close()
        return
    
    def returnColum(self, n):
        '''
        fetches the rigth values from the OTU object and 
        returns them as a list
        '''
        col = []
        first = True
        for line in self.OTU:
            f = line[n].strip()
            # type conversion of scientific annotation
            # as with mothur:
            '''
            the shared file only uses integers, any float 
            values will be rounded down to the nearest integer.
            '''
            if n != 0 and first != True:
                f = int(float(f))
            
            col.append(f)
            first =False

        return col
            
          
# call the class        
csv2shared(sys.argv[1], sys.argv[2], sep)
