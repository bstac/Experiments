def readAfile(fName):
    f = open(fName,'r')
    return f.read()

def rwAfile(strIn,fNameOut):
    f_out = open(fNameOut,'w')
    contents = str(strIn)
    f_out.write(contents)
    return 'Done!'

