height = 0
i = 1
blocks = int(input("Enter the number of blocks: "))

while i <= blocks :
    height +=1  
    blocks -=  i
    i += 1
      
print("The height of the pyramid:", height )