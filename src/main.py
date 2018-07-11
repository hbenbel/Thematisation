import classUtils
import ngrams
import os.path

def loadFile(path):
    with open(path, encoding='utf-8', errors='ignore') as f:
        text = f.readlines()
    text = list(filter(lambda x: x != '\n', text))
    return "".join(text)

def getThematics():
    thematicsList = []
    nbThematics = input("How many thematics do yout want to enter? ")
    for i in range(int(nbThematics)):
      name = input("Enter the name of the thematics " + str(i+1) + ": ")
      thematic = classUtils.Thematic(name, "")
        
      option = input("Enter a text or load an existing text? (1 = Manually; 2 = Load File) ")
      if (option == "1"):
        text = input("Enter a text for the thematic " + thematic.name + ": ")
        thematic.text = text
      elif (option == "2"):
        filepath = input("Enter the path of the file to load: ")
        if (os.path.exists(filepath)):
          thematic.text = loadFile(filepath)
        else:
          print("Wrong path :/")
      else:
        print("Wrong option :(")  
      thematicsList.append(thematic)
    return thematicsList

def validationNgrams(theme):
    fr = ngrams.freqs(theme.text)
    newNgram = []
    for f in fr:
      print(f)
      validation = input("Do you want to validate this n-gram? (yes/no)")
      if (validation.strip() == "yes" or validation.strip() == "y"):
        newNgram.append(f)
        print("This n-gram has been validated")
      elif (validation.strip() == "no" or validation.strip() == "n"):
        print("This n-gram has been deleted")
      else:
        print("Wrong answer :(")
    return newNgram


thematics = getThematics()
for theme in thematics:
  newNgram = validationNgrams(theme)
  print("\n",newNgram, "\n")
