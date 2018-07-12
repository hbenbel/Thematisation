import classUtils
import ngrams
import os.path
import operator

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
      validation = input("Do you want to validate this n-gram? (yes/no): ")
      if (validation.strip() == "yes" or validation.strip() == "y"):
        newNgram.append(f)
        print("This n-gram has been validated")
      elif (validation.strip() == "no" or validation.strip() == "n"):
        print("This n-gram has been deleted")
      else:
        print("Wrong answer :(")
    return newNgram


thematics = getThematics()
listofngram = []
listofthematics = []
for theme in thematics:
  print("\n\n")
  print("Validation for the theme", theme.name)
  newNgram = validationNgrams(theme)
  for ngram in newNgram:
      listofngram.append((ngram[0], theme.name))
      listofthematics.append((theme.name, 0))

dictngram = dict(listofngram)
dictofthematics = dict(listofthematics)
print(listofngram)

print("\n\n")
path = input("Enter the path of the text to thematize: ")
if (os.path.exists(path)):
    text = loadFile(path)
else:
    print("Wront path :/")

fr = ngrams.freqs(text)
for f in fr:
    if f[0] in dictngram:
        dictofthematics[f[1]] += 1

print("The closest category for this text is: ", max(dictofthematics.items(), key=operator.itemgetter(1))[0])
