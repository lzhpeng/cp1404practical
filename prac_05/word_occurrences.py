word_count = {}
text = input("Text: ")
words = text.split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

words = sorted(word_count.keys())

max_length = max(len(word) for word in words)

for word in words:
    print(f"{word:{max_length}} : {word_count[word]}")