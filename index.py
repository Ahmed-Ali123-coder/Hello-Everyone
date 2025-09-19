print("Hello form index file")
print("Welcome to git")

try : 
<<<<<<< HEAD
    with open("welcome.txt" , "+r") as file : 
=======
    with open("welcome.txt" , "+a") as file : 
        file.write("Writing someting in a file\n")
        file.seek(0)
>>>>>>> master
        for line in file : 
            print(line.strip())
except FileNotFoundError as ex :
    print("File not found error")