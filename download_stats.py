#clear file
def clearFile(filename):
    open(filename, 'w').close()

#print 1 element into the file
def downloadStats(filename,element):
    with open(filename, 'a') as f:
        f.write(element)

#print Array with size i,j,k into file
def printArray3D(filename,arrayname,i,j,k):
    for i1 in range(i):
        for j1 in range(j):
            for k1 in range(k):
                arrayelement=str(i1) + " " + str(j1) + " " + str(k1) + " " + str(arrayname[i1][j1][k1])+'\n'
                downloadStats(filename,arrayelement)
