import numpy as np 


print("Matrix Calculator")
print("------------------------------------------")

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

elements = []

print("Enter the elements of the matrix in rows form: ")

for i in range (rows):
    rows_num =  list(map(int, input(f"row {i+1}: ").split()))
    if len(rows_num) != cols : 
        print("Invalid number of elements ")
        exit()
    elements.append(rows_num)

newarr = np.array(elements, dtype="int32")


print("""What funtion do you want to perform! 
      1. To find deeterminent fo the matrix enter d :
    2.  TO find the transpose of the matrix press t  """)

while True : 
 user_= str(input("Enter the command : ")).strip().lower()

 if user_ != "d" and user_ != "t" : 
    print("Command not found ! ")
    continue 
 
 elif user_ == "d" : 
    if rows != cols : 
     print("Determinant of non squared matrix is not doable! ")
     break 

    print(np.linalg.det(newarr)) 
    
    break 
 elif user_ == "t": 
    print(newarr.T)
    break 
 

 elif user_ == " ": 
    pass
