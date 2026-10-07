word1 = input("Enter first word: ").strip().lower()
word2 = input("Enter second word: ").strip().lower()

if word1 == "" or word2 == "":
    print("Words cannot be empty")
elif len(word1) != len(word2):
    print("The words are not anagrams")
elif sorted(word1) == sorted(word2):
    print("The words are anagrams")
else:
    print("The words are not anagrams")