input_str = "this is a test string"

words = [word for word in input_str.split(" ")]

i = 0
while i < len(words):
    min_word = i
    for j in range(i + 1, len(words)):
        if words[j][0] < words[min_word][0]:
            min_word = j

        words[i], words[min_word] = words[min_word], words[i]

    i += 1
print(words)
