print("Hello form index file")
print("Welcome to git")

try:
    with open("welcome.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError as ex:
    print("File not found error")
