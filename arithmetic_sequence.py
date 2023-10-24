def getUserVal():
     n1 = int(input("Enter 1st Term (A1): "))
     n2 = int(input("Enter 2nd Term (A2): "))
     n3 = int(input("Enter 2rd Term (A3): "))
     n = int(input("Find (n): "))
     return n,n1,n2,n3
def sequence(n,n1,n2,n3):
    d1 = n2 - n1
    d2 = n3 - n2
    if d1 == d2:
        An = n1 + ((n - 1) * d1)
        print(f"The {n}th Term is {An}")
        return An
    else:
        print("Not a Arithmetic Sequence!")

def series(n,n1,n2,n3):
    An = sequence(n,n1,n2,n3)
    d1 = n2 - n1
    d2 = n3 - n2
    if d1 == d2:
        Sn = ((n1 + An)/2) * n
        print(f"The Sum of this sequence to (n) is {Sn}")
user = getUserVal()
sequence(user[0],user[1],user[2],user[3])
