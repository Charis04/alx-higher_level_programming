#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("object"):str.find("object") + 27] + " " + str[str.find("wi"):str.find("wi") + 4] + " " + str[str.find("Py"):str.find("Py") + 6]
print(str)
