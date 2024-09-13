text = input()

words = text.split()

longest_word = max(words, key=len)

length_of_longest_word = len(longest_word)

print(f"{longest_word} {length_of_longest_word}")
