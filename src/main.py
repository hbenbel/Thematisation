import classUtils
import os.path

def loadFile(path):
    with open(path, encoding='utf-8', errors='ignore') as f:
        text = f.readlines()
    text = list(filter(lambda x: x != '\n', text))
    return "".join(text)

def getThematics():
    thematicsList = []
    nbThematics = raw_input("How many thematics do yout want to enter ? ")
    for i in range(int(nbThematics)):
      name = raw_input("Enter the name of the thematics " + str(i) + ": ")
      thematic = classUtils.Thematic(name, "")
      thematicsList.append(thematic)

      for thematic in thematicsList:
	option = raw_input("Enter a text or load an existing text ? (1 = Manually; 2 = Load File) ")
	if (option == "1"):
          text = raw_input("Enter a text for the thematic " + thematic.name + ": ")
	  thematic.text = text
	elif (option == "2"):
	  filepath = raw_input("Enter the path of the file to load: ")
	  if (os.path.exists(filepath)):
	    thematic.text = loadFile(filepath)
	  else:
	    print("Wrong path :/")
	else:
	  print("Wrong option :(")
    return thematicsList

getThematics()
