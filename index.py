print("Hello form index file")
print("Welcome to git")

try : 
    with open("welcome.txt" , "r+") as file : 
        file.write("Hello from python and git\n")
        file.seek(0)
        for line in file : 
            print(line.strip())
except FileNotFoundError as ex :
    print("File not found error")