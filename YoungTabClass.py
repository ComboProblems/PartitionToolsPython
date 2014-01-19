from support import *
from Dimondtring import *
#### Highlight of this class is the latex for M-diagrams, web drawings, and tableau. 
class YoungTableau:
    """Assumes english conventions, the largest number of items as the top"""
    def __init__(self, rowlist):
        """Takes a list of lists, assuming the first list is the first row of the tableau"""
        ### self._data is the dictionary which the tableau is stored
        self._data = {}
        #### A list of each of the number of items in each row 
        self._rowlens = []
        #### Likewise for columns
        self._colunmlen = []
        #### Holds a copy of the tab for duplication reasons to be fixed in future versions
        self.duplicationuse = rowlist[:]
        #### Computes rowlens
        for i in xrange(len(rowlist)):
            self._data[i] = rowlist[i]
            self._rowlens += [len(rowlist[i])]
        self._dim = len(rowlist)
        #### What number is the tableau a partition of
        self._size = reduce(add, self._rowlens)
    def isStandard(self):
        """Checks if a standard tablux, returns bool"""
        a = range(1,self._size+1)
        for i in xrange(self._dim):
            if not increasing(self._data[i]):
                return False
            for j in self._data[i]:
                if j not in a:
                    return False
        j=0
        while j < len(self._data[0]):
            hold = []
            for i in xrange(self._dim):
                try:
                    hold += [self._data[i][j]]
                except IndexError:
                    pass
            if not increasing(hold):
                return False
            j += 1
        return True 
    def __repr__(self):
        #### Visual of tab
        string = ""
        for i in xrange(self._dim):
            if i != self._dim -1 :
                string += str(self._data[i]) + "\n"
            else:
                string += str(self._data[i])
        return string
    def __eq__(self, other):
        #Checks if two tabs 1. partition the same number 2. have the same shape. 3. have the same filling
        if self._size != other._size:
            return False
        else:
            for i in xrange(len(self._data)):
                for j in xrange(len(self._ data[i])):
                    try:
                        if self._data[i][j] != other._data[i][j]:
                            return False
                    except IndexError:
                        return False
                    except KeyError:
                        return False
        return True
    def __neq__(self, other):
        return not self.__eq__(other)
    def shape(self):
        """Returns the shape of the tableau as a list"""
        return self._rowlens
    def is_rec(self):
        """checks if a tableaux has a rectuangluar shape"""
        if len(self._rowlens) == len(filter(lambda k: self._rowlens[0] == k, self._rowlens)):
            return True
        else:
            return False
    def transpose(self):
        """Transposes and returns a new Tableaux"""
        new = {}
        for i in xrange(len(self._data[0])):
            new[i] = []
            for j in xrange(len(self._data)):
                try:
                    new[i] += [self._data[j][i]]
                except IndexError:
                    pass
        hold = []
        for i in new:
            hold += [new[i]]
        return YoungTableau(hold)
    def swap(self, a, b):
        """Alters the Tab, swaps two elements of a tab"""
        v , w = 0 , 0 ### Yearnest was here , location of a
        x, y = 0 , 0 ### Jenny sucks!, location of b 
        for i in self._data:
            for j in xrange(len(self._data[i])):
                if self._data[i][j] == a:
                    v , w = i, j
                if self._data[i][j] == b:
                    x , y = i, j
        self._data[v][w] = b
        self._data[x][y] = a
    def copy(self):
        """Copys a tab and retur ns a new one"""
        return self.transpose().transpose()
    def _makeWbury(self, word = [], display=False):
        ### Raises error if not standard and rec. Used in created latex output. Returns grid which cotains infomationfor digraming.
        #### Tab not needed, can be use with any word (string of numbers)
        ### Future, make this function not apart of class.
        if self.isStandard():
            if self.is_rec():
                if len(word) == 0:
                    word = self.createword()
                needsmorelists = []
                ### Create grid
                grid = {}
                testa = []
                for i in xrange(len(word)):
                    grid[i]= [0]*len(word)
                create = createtupnet(word)
                ###puts the word into grid
                for i in xrange(len(word)):
                    grid[i][i] = create[i]
                    if display:
                        if (i,i) not in needsmorelists:
                            testa += [grid[i][i]]
                            needsmorelists += [(i,i)]
                ### computes the westbury algorithm
                a = 1
                while a < len(word):
                    for i in xrange(a,len(word)):
                        for j in xrange(len(word) -a):
                            if type(grid[i-1][j]) is  tuple:
                                if type(grid[i][j+1]) is tuple:
                                    grid[i][j] = newtup(grid[i-1][j],grid[i][j+1])
                                    if display:
                                        if (i,j) not in needsmorelists:
                                            testa += [grid[i][j]]
                                            needsmorelists += [(i,j)]
                    a +=1
                if display:
                    return testa
                return grid
        else:
            raise TypeError
    #### Features pretty print, rep, visuals, operations (insert, remove, join), propeteries of tableaux
    ####
    def jeu(self):
        """returns a new tableau jue de teachaned, 0 is an empty block"""
        if not self.isStandard():
            raise TypeError
        ### Semistandard is less than or equal to
        self._data[0][0] = 0
        for i in xrange(len(self._data)):
            for j in xrange(len(self._data[i])):
                try:
                    if self._data[i][j] ==0:
                        if self._data[i+1][j] < self._data[i][j+1]:
                            self.swap(0,self._data[i+1][j])
                        else:
                            self.swap(0,self._data[i][j+1])
                except KeyError:
                    try:
                        self.swap(0,self._data[i][j+1])
                    except IndexError:
                        pass
                except IndexError:
                    try:
                        self.swap(0,self._data[i+1][j])
                    except KeyError:
                        pass
    def createword(self):
        word = []
        hold = []
        count = 0
        if not self.isStandard():
            raise TypeError
        for f in xrange(self._dim * len(self._data[0])):
            hold  += [f + 1]
        for i in xrange(self._dim):
            for k in self._data[i]:
                hold[k-1] = i+1
        return hold
##############################################################################################
##############################################################################################
##############################################################################################
############################Latex Stuff o    #################################################
##############################################################################################
##############################################################################################
##############################################################################################
    def export_M_diagram(self, filename="text.txt"):
        """Creates an M diagram"""
        if self.isStandard():
            if self.is_rec():
                pair = []
                for i in xrange(self._dim):
                    if i+1 == self._dim:
                        break
                    pair += [match(self._data[i],self._data[i+1])]
        b = self._size
        f = open(filename, 'w')
        f.write("\\begin{figure}[h] \n")
        f.write("\n\\begin{tikzpicture}[baseline=0cm, scale=1]")
        ##f.write("\n\\draw[style= ultra thick, ->] (" + str(float(9-b)/2) + ",0)--(" + str(float(9-b)/2 + .75)+ ",0);")
        f.write("\n\\draw[style=thick] (" +  str(6 - float(b)/2)  + ",-.7)--("+str(6+ float(b)/2)+",-.7);")
        for i in xrange(self._size):
            f.write("\n\\node at ("+ str(6 - float(b)/2 + i + .5 ) +",-1.1) {" + str(i+1) + "};")
            f.write("\n\\draw[radius=.08, fill=black](" +str(6 - float(b)/2 + i + .5) + ",-.7)circle;")
        for i in pair: 
            for j in i:
                d =float(j[0]+j[1])/2 ### Loc
                e =float(abs(j[0]-j[1]))/2
                f.write("\n\\draw ("+ str(6 - float(b)/2  + .5 + j[1] - 1)+",-.7) arc (0:180: "+str(e)+"cm);")
        f.write("\n\\end{tikzpicture}\n\\end{figure}")
        f.close()
##############################################################################################
##############################################################################################
    def exportWWeb(self, word = [], filename="output.txt", gridlines=True, style="style=dashed", flip=False, cross=False,dirlist=["{postaction={decorate},decoration={markings,mark=at position .55 with {\\arrow{>}}}}","style= double","{postaction={decorate},decoration={markings,mark=at position .55 with {\\arrow{<}}}}"]):
        #### Writes a LaTeX code for making a westbury diagram from a tabluaux
        if len(word) > 0:
            data = self._makeWbury(word, True)
            j = len(word)
        if len(word)== 0:
            data = self._makeWbury(word, True)
            j = self._size ### Used a counter for pos in list
        if data is False:
            return None
        #### Creates the data structure with infomation encoded in the web
        f = open(filename, 'w')
        f.write("\\begin{figure}[h] \n")
        f.write("\n\\begin{tikzpicture}[baseline=0cm, scale=1]")
        count = 0 ### counter or when to step down
        
        k = j ### location on graph
        def writetupe(tup,k,count, dirlist, flip=False):
            ### Writes the web part of the diagram for both triangle and diamonds
            h = 1 #if h is one, the triangles will be ont op? I think
            if flip:
                h = -1
            a = (-float(k+1)/2+count-.25 +1,h* (float(k)/2 + .25))
            b = (-float(k+2)/2+count+.75 +1, h*(float(k)/2 + .25))
            c = (-float(k+1)/2+count-.25 +1,h* (float(k)/2 - .25))
            d = (-float(k+2)/2+count+.75 +1, h*(float(k)/2 - .25))
            e = (-float(k+1)/2+count +1, h*(float(k)/2 + 1.0/8))
            g = (-float(k+1)/2+count +1, h*(float(k)/2 - 1.0/8))
            da = 0 #for chcking if the first iteration
            lenst = len(dirlist) + 1
            for i in tup:
                if i == 0:
                    da += 1
            if da> 3:
                return 
            if da == 3:
                if tup[0] == 0:
                    if tup[1] !=0:
                        f.write("\n\\draw[" + str(dirlist[0]) + "](" + str(-float(k+1)/2+count +1) + "," + str(h*(float(k)/2)) + ")--(" + str(g[0]) + "," + str(g[1]) + ");")
                        f.write("\n\\draw[" + str(dirlist[tup[1]-1]) + "](" + str(g[0]) + "," + str(g[1]) +")--(" + str(d[0]) + "," + str(d[1]) + ");")
                        return
            if da == 3:
                if tup[1] == 0:
                    if tup[0]!= 0:
                        f.write("\n\\draw[" + str(dirlist[0]) + "](" + str(-float(k+1)/2+count+1) + "," + str(h*(float(k)/2)) +  ")--(" + str(g[0]) + "," + str(g[1]) + ");")
                        f.write("\n\\draw[" + str(dirlist[ lenst-tup[0]  -1]) + "](" + str(g[0]) + "," + str(g[1]) +")--(" + str(c[0]) + "," + str(c[1]) + ");")
                        return 
            if da == 2:
                if tup[1] != tup[0]:
                    if tup[0] != 0:
                        if tup[1] !=0:
                            f.write("\n\\draw[" + str(dirlist[0]) + "](" + str(-float(k+1)/2+count+1) + "," + str(h*(float(k)/2)) +  ")--(" + str(g[0]) + "," + str(g[1]) + ");")
                            f.write("\n\\draw[" + str(dirlist[tup[0]  -1]) + "](" + str(-float(k+1)/2+count-.25 +1 ) + "," + str(h*(float(k)/2 - .25)) + ")--(" + str(g[0]) + "," + str(g[1]) + ");")
                            f.write("\n\\draw[" + str(dirlist[tup[1]-1]) + "](" + str(g[0]) + "," + str(g[1]) +")--(" + str(d[0]) + "," + str(d[1]) + ");")
                            return
    
            if tup[3] == tup[2]:
                f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(-float(k+1)/2+count-.25 +1 )+","+str(h*(float(k)/2 + .25)) + ")--(" + str(-float(k+1)/2+count +1) + "," + str(h*(float(k)/2 + 1.0/8)) +");")
                f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(-float(k+1)/2+count +1) + "," + str(h*(float(k)/2 + 1.0/8)) +")--(" + str(-float(k+2)/2+count+.75 +1) + "," + str(h*(float(k)/2 + .25)) + ");")
                return
            elif da== 2:
                if tup[3] == 0:
                    f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(c[0]) + "," + str(c[1])+")--("+ str(b[0] ) + "," + str(b[1]) + ");")
                    return
                if tup[2] ==0:
                    f.write("\n\\draw[" + str(dirlist[tup[3]-1]) + "](" + str(a[0]) + "," + str(a[1])+")--("+ str(d[0] ) + "," + str(d[1]) + ");")
                    return
            elif tup[2] != tup[3]:
            
                f.write("\n\\draw[" + str(dirlist[((tup[2]-tup[3] )%lenst) - 1]) +"]("+ str(g[0]) + "," + str(g[1])+")--("+ str(e[0]) + "," + str(e[1]) + ");")
                f.write("\n\\draw[" + str(dirlist[tup[3]-1]) + "](" + str(a[0]) + "," + str(a[1])+")--("+ str(e[0] ) + "," + str(e[1]) + ");")
                f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(e[0]) + "," + str(e[1])+")--("+ str(b[0] ) + "," + str(b[1]) + ");")
                f.write("\n\\draw[" + str(dirlist[tup[3]-1]) + "](" + str(g[0]) + "," + str(g[1])+")--("+ str(d[0] ) + "," + str(d[1]) + ");")
                f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(c[0]) + "," + str(c[1])+")--("+ str(g[0] ) + "," + str(g[1]) + ");")
                return 
        def makeDimond(k, count, flip=False):
            #### Creates the bottom part of a triangle
            h = 1
            if flip:
                h = -1
            f.write("\n\\draw["+ str(style) +"]("+str(-float(k)/2 + count+1)+"," + str(h*(float(k)/2))+")--("+str(-float(k+1)/2+count +1)+"," + str(h*(float(k)/2-.5))+")--("+str(-float(k+2)/2 + count +1)+"," + str(h*(float(k)/2))+");")         
        for i in xrange(len(data)):
            if count == j:
                count = 0
                j -= 1
                k = j
            if j == self._size:
                if gridlines:
                    h = 1
                    if flip:
                        h = -1
                    ### Makes a triangle at the top###
                    f.write("\n\\draw["+ str(style) +"]("+ str(-float(k)/2 + i)+","+str(h*(float(k)/2))+")--("+str(-float(k)/2 + i+1)+ "," +str(h*(float(k)/2))+");")
                    f.write("\n\\draw["+ str(style) +"]("+str(-float(k)/2 + i+ .5)+","+str(h*(float(k)/2-.5))+")--("+ str(-float(k)/2 + i)+","+str(h*(float(k)/2))+");")
                    f.write("\n\\draw["+ str(style) +"]("+str(-float(k)/2 + i+ .5)+","+str(h*(float(k)/2-.5))+")--("+ str(-float(k)/2 + i +1)+","+str(h*(float(k)/2))+");")
                if cross: #cross draws w lines crossing
                    if flip:
                        writeCross(sdata[i],k,count, dirlist, f, True)
                    else:
                        writeCross(data[i],k,count, dirlist, f)
                else:
                    if flip:
                        writetupe(data[i],k,count, dirlist,True)
                    else:
                        writetupe(data[i],k,count, dirlist)
            else:
                if gridlines: #makes dimongridlines
                    if flip:
                        makeDimond(k,count,True)
                    else:
                        makeDimond(k,count)
                if cross:
                    if flip:
                        writeCross(data[i],k,count, dirlist, f, True)
                    else:
                        writeCross(data[i],k,count, dirlist, f)
                else:
                    if flip:
                        writetupe(data[i],k,count, dirlist, True)
                    else:
                        writetupe(data[i],k,count, dirlist)
            count += 1
        f.write("\n\\end{tikzpicture}\n\\end{figure}")
        f.close()
##############################################################################################
        ##############################################################################################
        ##############################################################################################
        ##############################################################################################
        ##############################################################################################
        ##########Possible bug for tab wiht one column####################################################################################
        ##############################################################################################
    def exportTab(self, filename= "tab.txt"):
        f = open(filename, 'w')
        f.write("\\begin{table}[h]\n\\begin{tabular}{")
        for i in self._data[0]:
            f.write(" c")
        f.write("} \n \\hline \n")
        for i in self._data:
            for j in xrange(len(self._data[i])):
                f.write("\multicolumn{1}{|c|}{" +str(self._data[i][j]) + "}")
                if j == len(self._data[i]) -1:
                    f.write("\\\ \n \\cline{1-" + str(len(self._data[i]))+"} \n")
                else:
                    f.write(" & ")
        
        f.write("\\end{tabular} \n \\end{table}")
        f.close()
    
##class Standard_Young(YoungTableau):

##    if not YoungTableau.isStandard():
##        raise TypeError
