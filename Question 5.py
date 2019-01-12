print("Anas Ahmed - 18B-116-CS - Sec 'A'")
print(" LAB 4 -9 Nov 2018")
print("question - 5")

initial_value = eval(input("Enter the initial value for the range :"))
final_value = eval(input("Enter the final value for the range :"))
numbers = range(initial_value,final_value+1)
sum = 0

for value in numbers:
    sum = sum + value

print("the sum is",sum)    
