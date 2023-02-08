# This code prompts the user to enter a sentence,
# then prompts the user to enter two words.
# It then replaces the first word with the second
# word in the sentence and prints out the modified sentence.

sentence = input('Enter your sentence: ')
print('Your sentence is ' + sentence)
word1 = input('Enter the word to replace : ')
word2 = input('Enter the word to replace it with : ')
print(sentence.replace(word1, word2))
