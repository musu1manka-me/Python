# def changeFirstLetter(words,letters):
#     new_word = []
#     for v in range(len(words)):
#         new_word.append(letters[v]+words[v][1:])
#     return " ".join(new_word)    



# def shiftsentence(sentence):
#     words = sentence.split(" ")
#     letters = [ v[0] for v in words]
#     letters.insert(0,letters[len(letters)-1])
#     letters.pop(len(letters)-1)
#     return changeFirstLetter(words,letters)
# print(shiftsentence("create a function"))


# def is_Happy_num(n):
#   past = set()
#   while n != 1:
#         n = sum(int(i)**2 for i in str(n))
#         if n in past:
#             return False
#         past.add(n)
#   return True
# print(is_Happy_num(7))
# print(is_Happy_num(932))
# print(is_Happy_num(6))




