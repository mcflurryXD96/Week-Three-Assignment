# Daniel McMurray
# pig.py
# English to PigLatin Word Translation

# Prompt the user to enter an English word to translate

word = input("Enter an English word to translate: ")

# Program determines whether first letter is a vowel or a consonant

vowel = "aAeEiIoOuU"     # This fixes the case sensitivity issue with words starting with vowels only

if word[0] in vowel:
    print(word+"yay")
else:
    print(word[1:]+word[0]+"ay")