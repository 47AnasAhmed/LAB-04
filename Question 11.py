print("Anas Ahmed - 18B-116-CS - Sec 'A'")
print(" LAB 4 -9 Nov 2018")
print("question - 11")

print("The program will count total number of vowels from user defined sentence")
string = input("Enter the string:")
vowels = 0

for i in string:
    if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E' or i=='I'or i=='O'or i=='U'):
        vowels=vowels+1
    
        if i in 'aeiouAEIOU':
            print(i)
            
print("Number of vowels are:")
print(vowels)
