#without replace()
 
with open("bookmarks.html") as f:
    data = f.read()
    tagindex = data.find("test")

    tagindexLower = tagindex -50
    tagindexHigher = tagindex +50

print(data)
print(data[tagindexLower:tagindexHigher])
