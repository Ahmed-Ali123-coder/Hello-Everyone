print("Hello form index file")
print("Welcome to git")

try : 
    with open("welcome.txt" , "r+") as file : 
        print(file.read)
except FileNotFoundError as ex :
    print("File not found error")