database = ["A","B","C","D"]

print("\n A \n B \n C \n D")

goal = input("Enter the Goal :")

if goal == "A":
    print("A is the Initial Fact")

elif goal == "B":
    print("B <- A")

elif goal == "C":
    print("C <- B")
    print("B <- A")

elif goal == "D":
   print("D <- C")
   print("C <- B")
   print("B <- A")
   
else :
    print("Invalid Input")
    
