database = ["A","B","C","D"]
print("Forwar Chaining ")
print("\n 1.A \n 2.B \n 3.C \n 4.D")
n=int(input("Enter the Raw Data Number: "))
if n == 1:
    print("A->B")
elif n == 2:
    print("B->C")
elif n == 3:
    print("C->D")
elif n == 4:
    print("D Goal Reached")
else:
    print("Invalid INput")

if n>=1 and n<=4:
    print("Selected : ",database[n-1])
