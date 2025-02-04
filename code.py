all =  ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
setnence = ""
smth = str(input("Enter whatever values you want to implement"))
for each in smth:
    if each in all:
        new = all[(all.index(each)+3)%26]
        setnence += new
print(setnence)

