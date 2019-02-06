from collections import Counter
count = Counter()
text = "this is a text this"
for word in text.split():
    count[word] += 1

print(count)