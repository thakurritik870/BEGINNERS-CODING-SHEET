#) Write a Program to Check Whether a Character is Vowel or Consonant.

vowels = ('a', 'i', 'e', 'o', 'u')

x = input("Enter a character: ")

if x.lower() in vowels:
    print("Vowel")
else:
    print("Consonant")
