import classUtils
import codecs

def loadFile(path):
    with codecs.open(path, 'r', 'utf-8', 'ignore') as text:
        return text.read()

def getThematics():
    thematicsList = []
    nbThematics = input("How many thematics do yout want to enter ? ")
    for i in range(int(nbThematics)):
        name = input("Enter the name of the thematics " + str(i) + ": ")
        thematic = classUtils.Thematic(name, "")
        thematicsList.append(thematic)

    for thematic in thematicsList:
        option = input("Enter a text or load an existing text ? (1 = Manually; 2 = Load File)")
        if (option == "1"):
            text = input("Enter a text for the thematic " + thematic.name + ": ")
            thematic.text = text
        elif (option == "2"):
            filepath = input("Enter the path of the file to load: ")
            thematic.text = loadFile(filepath)
        else:
            print("Wrong option :(")

    return thematicsList
