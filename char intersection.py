
Phase1 = input("Enter the first sentence: ")
Phase2 = input("Enter the second sentence: ")


words_phrase1 = set(Phase1.lower().split())
words_phrase2 = set(Phase2.lower().split())


intersection = words_phrase1.intersection(words_phrase2)


ordinate_intersection = [words for words in Phase1.split() if words.lower() in intersection]


print(" ".join(ordinate_intersection))
