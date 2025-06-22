word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

wordSum1 = 0
wordSum2 = 0

for char in word1:
    wordSum1 += ord(char)

for char in word2:
    wordSum2 += ord(char)

if (word1 > word2):
    print("'" + word2 + "' appears in the dictionary first.")

elif (word1 < word2):
    print("'" + word1 + "' appears in the dictionary first.")

else:
    print("The two words are the same.")

print('Difference in ASCII value:', abs(wordSum1 - wordSum2))
