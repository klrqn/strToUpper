#! python3
# program that uppercases all text from the clipboard

import pyperclip
text = pyperclip.paste()
tempList = []

for i in range(len(text)):
    # tempList.append(text[i].upper())
    # print(text[i].upper())
    tempList.append(text[i].upper())

print(tempList)
newtext = ''
newtext.join(tempList)

print(newtext)

pyperclip.copy(newtext)
