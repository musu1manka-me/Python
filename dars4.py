# str_word = "The pop() method removes The item with the specified key name"
# dct = {}
# for v in str_word:
#     if(v.isalpha()):
#         if(v.lower() in dct):

#             dct[v] = str_word.count(v)
# print(dct)





myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Hemil",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2008
  },
  "child4" : {
    "name" : "Torus",
    "year" : 2001
  }
}
for child in myfamily:
    if(myfamily[child]["year"] >= 2005):

      print(myfamily[child]["name"])
      