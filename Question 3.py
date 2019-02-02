print("Anas Ahmed")
print("18B-116-CS(A)")
print("Lab - 04")
print("Programming Ex: 3")

print("\n\nPalindrome Test\n")

user_str = input("Please enter the word to check if its palindrome:")
user_str = user_str.lower()
if user_str == user_str[::-1]:
    print("This is a palindrome!")
else:
    print("Sorry this is not a Palindrome!")
