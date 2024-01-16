input_string = input("Введите строку: ")
words = input_string.split()
unique_words = sorted(set(words))
for word in unique_words:
    print(word)