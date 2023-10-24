sentence = "Python is a programming language"

new_str = sentence.split(" ")


small_word = new_str[0]
large_word = new_str[0]


for word in new_str:
    if len(small_word) > len(word):
        small_word = word
    elif len(large_word) < len(word):
        large_word = word

# print(new_str)
print("Smallest word: ", small_word)
print("Largest word: ", large_word)
