def makething(edgetype, height  = 1, pos = 0, border = True, flip=False, filename = "outputDi.txt", style ="dashed", dirlist=["{postaction={decorate},decoration={markings,mark=at position .55 with {\\arrow{>}}}}","style= double","{postaction={decorate},decoration={markings,mark=at position .55 with {\\arrow{<}}}}"]):
    f = open(filename, 'w')
    f.write("\\begin{figure}[h] \n")
    f.write("\n\\begin{tikzpicture}[baseline=0cm, scale=1]")
    if flip:
        if writetup(edgetype, height , pos, dirlist, f, True):
            if border:
                drawtri(height , pos, style, f, True)
        else:
            if border:
                makeDimond(height , pos, style, f, True)
    else:
        if writetup(edgetype, height , pos, dirlist, f, False):
            if border:
                drawtri(height  , pos, style, f, False)
        else:
            if border:
                makeDimond(height  , pos, style, f, False)
    f.write("\n\\end{tikzpicture}\n\\end{figure}")
    f.close()    
    
    
def writetup(tup,k,count, dirlist, f, flip=False):
    h = 1
    if flip:
        h = -1
    a = (-float(k+1)/2+count-.25 +1, h* (float(k)/2 + .25))
    b = (-float(k+2)/2+count+.75 +1, h*(float(k)/2 + .25))
    c = (-float(k+1)/2+count-.25 +1, h* (float(k)/2 - .25))
    d = (-float(k+2)/2+count+.75 +1, h*(float(k)/2 - .25))
    e = (-float(k+1)/2+count +1, h*(float(k)/2 + 1.0/8))
    g = (-float(k+1)/2+count +1, h*(float(k)/2 - 1.0/8))
    da = 0
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
                return True
    if da == 3:
        if tup[1] == 0:
            if tup[0]!= 0:
                f.write("\n\\draw[" + str(dirlist[0]) + "](" + str(-float(k+1)/2+count+1) + "," + str(h*(float(k)/2)) +  ")--(" + str(g[0]) + "," + str(g[1]) + ");")
                f.write("\n\\draw[" + str(dirlist[ lenst-tup[0]  -1]) + "](" + str(g[0]) + "," + str(g[1]) +")--(" + str(c[0]) + "," + str(c[1]) + ");")
                return True
    if da == 2:
        if tup[1] != tup[0]:
            if tup[0] != 0:
                if tup[1] !=0:
                    f.write("\n\\draw[" + str(dirlist[0]) + "](" + str(-float(k+1)/2+count+1) + "," + str(h*(float(k)/2)) +  ")--(" + str(g[0]) + "," + str(g[1]) + ");")
                    f.write("\n\\draw[" + str(dirlist[tup[0]  -1]) + "](" + str(-float(k+1)/2+count-.25 +1 ) + "," + str(h*(float(k)/2 - .25)) + ")--(" + str(g[0]) + "," + str(g[1]) + ");")
                    f.write("\n\\draw[" + str(dirlist[tup[1]-1]) + "](" + str(g[0]) + "," + str(g[1]) +")--(" + str(d[0]) + "," + str(d[1]) + ");")
                    return True
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
                            
def makeDimond(k, count, style, f, flip=False):
    h = 1
    if flip:
        h = -1
    f.write("\n\\draw["+str(style)+"]("+str(-float(k)/2 + count+1)+"," + str(h*(float(k)/2))+")--("+str(-float(k+1)/2+count+1)+"," + str(h*(float(k)/2+.5))+")--("+str(-float(k+2)/2 + count +1)+"," + str(h*(float(k)/2))+")--("+str(-float(k+1)/2+count +1)+"," + str(h*(float(k)/2-.5))+")--("+str(-float(k)/2 + count +1)+"," + str(h*(float(k)/2))+")-- cycle;")
                            
def drawtri(k, i, style, f, flip=False):
    h = 1
    if flip:
        h = -1
    f.write("\n\\draw["+ str(style) +"]("+ str(-float(k)/2 + i)+","+str(h*(float(k)/2))+")--("+str(-float(k)/2 + i+1)+ "," +str(h*(float(k)/2))+");")
    f.write("\n\\draw["+ str(style) +"]("+str(-float(k)/2 + i+ .5)+","+str(h*(float(k)/2-.5))+")--("+ str(-float(k)/2 + i)+","+str(h*(float(k)/2))+");")
    f.write("\n\\draw["+ str(style) +"]("+str(-float(k)/2 + i+ .5)+","+str(h*(float(k)/2-.5))+")--("+ str(-float(k)/2 + i +1)+","+str(h*(float(k)/2))+");")

def writeCross(tup,k,count, dirlist, f, flip=False):
    h = 1
    if flip:
        h = -1
    a = (-float(k+1)/2+count-.25 +1, h* (float(k)/2 + .25))
    b = (-float(k+2)/2+count+.75 +1, h*(float(k)/2 + .25))
    c = (-float(k+1)/2+count-.25 +1, h* (float(k)/2 - .25))
    d = (-float(k+2)/2+count+.75 +1, h*(float(k)/2 - .25))
    e = (-float(k+1)/2+count +1, h*(float(k)/2 + 1.0/8))
    g = (-float(k+1)/2+count +1, h*(float(k)/2 - 1.0/8))
    da = 0
    lenst = len(dirlist) + 1
    for i in tup:
        if i == 0:
            da += 1
    if da> 3:
        return
    if da == 3:
        if tup[0] == 0:
            if tup[1] !=0:
                f.write("\n\\draw[" + str(dirlist[0]) + "](" + str(-float(k+1)/2+count +1) + "," + str(h*(float(k)/2)) + ")--(" + str(d[0]) + "," + str(d[1]) + ");")
                return True
    if da == 3:
        if tup[1] == 0:
            if tup[0]!= 0:
                f.write("\n\\draw[" + str(dirlist[0]) + "](" + str(-float(k+1)/2+count+1) + "," + str(h*(float(k)/2)) +  ")--(" + str(c[0]) + "," + str(c[1]) + ");")
                return True
    if da == 2:
        if tup[1] != tup[0]:
            if tup[0] != 0:
                if tup[1] !=0:
                    f.write("\n\\draw[" + str(dirlist[tup[1]-1]) + "](" + str(-float(k+1)/2+count+1) + "," + str(h*(float(k)/2)) +  ")--(" + str(d[0]) + "," + str(d[1]) + ");")
                    f.write("\n\\draw[" + str(dirlist[tup[0]-1]) + "](" + str(c[0]) + "," + str(c[1]) +  ")--(" + str(-float(k+1)/2+count+1) + "," + str(h*(float(k)/2))+ ");")
                    return True
    if tup[3] == tup[2]:
        f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(-float(k+1)/2+count-.25 +1 )+","+str(h*(float(k)/2 + .25)) + ")--(" + str(-float(k+1)/2+count +1) + "," + str(h*(float(k)/2)) +");")
        f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(-float(k+1)/2+count +1) + "," + str(h*(float(k)/2)) +")--(" + str(-float(k+2)/2+count+.75 +1) + "," + str(h*(float(k)/2 + .25)) + ");")
        return
    elif da== 2:
        if tup[3] == 0:
            f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(c[0]) + "," + str(c[1])+")--("+ str(b[0] ) + "," + str(b[1]) + ");")
            return
        if tup[2] ==0:
            f.write("\n\\draw[" + str(dirlist[tup[3]-1]) + "](" + str(a[0]) + "," + str(a[1])+")--("+ str(d[0] ) + "," + str(d[1]) + ");")
            return
    elif tup[2] != tup[3]:
        f.write("\n\\draw[" + str(dirlist[tup[3]-1]) + "](" + str(a[0]) + "," + str(a[1])+")--("+ str(d[0] ) + "," + str(d[1]) + ");")
        f.write("\n\\draw[" + str(dirlist[tup[2]-1]) + "](" + str(c[0]) + "," + str(c[1])+")--("+ str(b[0] ) + "," + str(b[1]) + ");")
        return

def makethingscross(edgetype, height  = 1, pos = 0, border = True, flip=False, filename = "outputDi2.txt", style ="dashed", dirlist=["{postaction={decorate},decoration={markings,mark=at position .55 with {\\arrow{>}}}}","style= double","{postaction={decorate},decoration={markings,mark=at position .55 with {\\arrow{<}}}}"]):
    f = open(filename, 'w')
    f.write("\\begin{figure}[h] \n")
    f.write("\n\\begin{tikzpicture}[baseline=0cm, scale=1]")
    if flip:
        if writeCross(edgetype, height , pos, dirlist, f, True):
            if border:
                drawtri(height , pos, style, f, True)
        else:
            if border:
                makeDimond(height , pos, style, f, True)
    else:
        if writeCross(edgetype, height , pos, dirlist, f, False):
            if border:
                drawtri(height  , pos, style, f, False)
        else:
            if border:
                makeDimond(height  , pos, style, f, False)
    f.write("\n\\end{tikzpicture}\n\\end{figure}")
    f.close()
def stich(perm, kmax, dirlist, f, flip=False):
    """perm is simple permenation, k max is lenght of lat word """
    ###cornners a-d of a square, h,g are points in the square
##    a =
##    b =
##    c =
##    d =
##    h =
##    g =
##    f.write("
##    f.write()
##    
    pass
