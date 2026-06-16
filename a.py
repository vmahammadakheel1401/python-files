with open("file.txt", "w") as file:
    file.write("Hello, World!")
    file.write("this is a test file.")
with open("file.txt", "r") as file:
    count=0
    for line in file:
        count+=1
print("Number of lines in the file:", count)    


