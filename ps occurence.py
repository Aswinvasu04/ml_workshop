def find_occurence(text,word):
    words=text.split()
    count=words.count(word)
    return count

text="hello guys welcome guys who are u guys"
word="guys"
n = find_occurence(text,word)
print(n,"is the number of times",word,"repeated")
