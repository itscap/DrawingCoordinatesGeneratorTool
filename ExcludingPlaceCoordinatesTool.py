

import rlcompleter 
    

def deleteContent(file):
    file.seek(0)
    file.truncate()
    
def getUsrInput():
    print ("Insert X coordinate of the column you want to exclude:")
    colX=int(input())
    print ("Insert Y min:")
    fromY=int(input())
    print ("Insert Y max:")
    toY=int(input())

    print("Coordinates:\n X--> "+ str(colX) + "\nY--> From Y= "+str(fromY)+" to Y= "+str(toY))
    print("Confirm? Y/N")
    usrChoice=input()
    
    if usrChoice.lower() == "y":
        return [colX,fromY,toY]
    else: 
        getUsrInput()

def columnToExclude(coord):
    for y in range(coord[1],coord[2],1):
        textFile.write("("+ str(coord[0]) + "," +  str(y) + "),")

def excludeNewColumn():
    coordToExclude = getUsrInput()
    columnToExclude(coordToExclude)
    textFile.write("("+ str(coordToExclude[0]) + "," +  str(coordToExclude[2]) + ")")
    print("Do you want to exclude a new column? Y/N")
    usrChoice=input()
    if usrChoice.lower()=="y":
        textFile.write(",")
        excludeNewColumn()
    else:
        textFile.write("]")
    

        
#EX--> drawingName = [(colX,fromY),(133,481),(133,482),...(133,509),(colX,toY)]

fileToWriteName= "coordToExclude.txt"
drawingToExcludeName = "drawingName"
fromY=0
toY=0
colX =0
        

print ("Open file: " + fileToWriteName)
textFile = open(fileToWriteName, "a")
print ("Deleting previous file content...")
deleteContent(textFile)

textFile.write(drawingToExcludeName + " = [")
excludeNewColumn()
textFile.close()


print ("Done.")