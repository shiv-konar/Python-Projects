import re
# Check if a substring exists within a string
if re.search("ape", "The ape was at apex"):
    print "There is an ape"
else:
    print "ape not found"

# Find all occurences of a substring within a string
allApes = re.findall("ape", "The ape was at apex")
print type(allApes)  # list type

for i in allApes:
    print i

# Using a period, you can match exactly one character or one white space
allApeWords = re.findall("ape.", "The ape was at apex")

for i in allApeWords:
    print i.strip()

# Find starting and ending index of a substring
theStr = "The ape was at apex"

for i in re.finditer("ape.", theStr):   # finditer returns an iterator
    locTuple = i.span()  # span returns a tuple
    print locTuple
    print theStr[locTuple[0]:locTuple[1]]