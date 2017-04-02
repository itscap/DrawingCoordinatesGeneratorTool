
#EX. waldo_face = (133,480),(133,481),(133,482),(133,483)

def deleteContent(file):
    file.seek(0)
    file.truncate()

fileToWriteName= "coordToExclude.txt"
drawingToExcludeName = "drawName"
fromX = 133
toX=134
fromY=480
toY=509

print ("Open file: " + fileToWriteName)
textFile = open(fileToWriteName, "a")

print ("Deleting previous file content")
deleteContent(textFile)

print ("Write to file...")
textFile.write(drawingToExcludeName + " = [")

for x in range(fromX,toX+1,1):
    for y in range(fromY,toY,1):
        textFile.write("("+ str(x) + "," +  str(y) + "),")
    #textFile.write('\n')
        
textFile.write("("+ str(toX) + "," +  str(toY) + ")]")

textFile.close()
print ("Done.")