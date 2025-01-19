#WAP to print different vowels present in the given word

word = input("Enter a word: ")

vowels = "aeiouAEIOU"

# Creating a set to store the vowels which we find in the word
found_vowels = set()

# Iterating through each character (char) in the word
for char in word:
    if char in vowels:
        found_vowels.add(char)

print("Vowels present in the word are:", found_vowels)