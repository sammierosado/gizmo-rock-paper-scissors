file_object = open('article.txt', "r")
for line in file_object:
    words = line.lower().split()
    print(words)
