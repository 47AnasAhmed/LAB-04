print("Anas Ahmed")
print("18B-116-CS(A)")
print("Lab - 04")
print("Programming Ex: 2")

print("\nArithmetic Sequence\n\n")

def arithmetic_sq(y,z):
    
    n = eval(input("Please enter the number of the term you want to find: "))
    an = y+((n-1)*z)
    print("The",str(n),"th term in the given sequence is              :",str(an))
    user=input("\nDo you want to find another term? (Press 'y' to continue, 'q' to quit):")
    if user=='y':
        arithmetic_sq(y,z)
    else:
        print("Goodbye!")
    

a= eval(input("Please enter the first term in the sequence         : "))
d= eval(input("Please enter the common difference in the sequence  : "))

arithmetic_sq(a,d)



    

    
