f = open("addressBook\Book.txt", "w+")
d = open("addressBook\data.txt", "w+")
name = input("Hello! Please type your own name: ")
f.write(name + "'s Address Book\n\n")
d.write("BookName:"+ name + "\n")
f.close()
d.close()

f = open("addressBook\Book.txt", "a+")
d = open("addressBook\data.txt", "a+")

conNum = 0

def newItem(uName, uAddress, uPhone):
    global f
    global d
    global conNum
    conNum += 1
    uName = str(uName)
    uAddress = str(uAddress)
    dict = {
        "name": uName,
        "address": uAddress,
        "number": uPhone,
    }
    d.write(";" + str(conNum) + "\n")
    d.write("Name:" + dict["name"] + "\n")
    d.write("Address:" + dict["address"] + "\n")
    d.write("Number:" + dict["number"] + "\n")

    return dict

def editContact(num): #fix
    global d
    d.close()
    d = open("addressBook\data.txt", "a+")
    d.seek(0)
    page = d.readlines()
    num = ";" + num
    print(num)
    iterNum = -1
    for x in page:
        iterNum += 1
        location = x.find(str(num))
        if location > -1:
            break
    page[iterNum + 1] = "Name:" + input("Please input contact's Name: ") + "\n"
    page[iterNum + 2] = "Address:" + input("Please input contact's Address: ") + "\n"
    page[iterNum + 3] = "Number:" + input("Please input contact's Number: ") + "\n"

    d.close()
    d = open("addressBook\data.txt", "w+")
    d.writelines(page)
    d.close()
    d = open("addressBook\data.txt", "a+")
                


def deleteItem(search):
    global conNum
    found = False
    d = open("addressBook\data.txt", "a+")
    searchFor = ";" + str(search)
    d.seek(0)
    page = d.readlines()
    iterNum = -1
    iter = -1
    for x in page:
        iterNum += 1
        location = x.find(str(searchFor))
        if location > -1:
            break
    num = 4
    try:
        while num > 0:
            num -= 1
            del page[iterNum]
    except:
        print("No address assigned to that number...")
    d.close()
    d = open("addressBook\data.txt", "w+")
    d.writelines(page)


def writeToBook():
    global f
    global d
    d.seek(0)
    page = d.readlines()
    newPage = f.readlines()
    print(page)
    iterNum = -1
    for x in page:
        iterNum += 1
        if page[iterNum][0:1] == ";":
            if iterNum != 0:
                f.write("---- " + page[iterNum][1:2] + " ----\n")
        if page[iterNum][0:4] == "Name" and page[iterNum][5:] != "":
            f.write("Name - " + str(page[iterNum][5:]))
        if page[iterNum][0:7] == "Address" and page[iterNum][8:] != "":
            f.write("Address - " + str(page[iterNum][8:]))
        if page[iterNum][0:6] == "Number" and page[iterNum][7:] != "":
            f.write("Number - " + str(page[iterNum][7:]))
        page[iterNum]
        f.write("")


while True:
    choice = input("Would you like to  1 - create new contact, 2 - edit an existing contact, or 3 - delete a contact? ")
    if choice == "1":
        newDict = newItem(input("Type contact's name: "), input("Type contact's Address: "), input("Type contact's Number: "))
    elif choice == "2":
        d.close()
        f.close()
        d = open("addressBook\data.txt", "a+")
        f = open("addressBook\Book.txt", "a+")
        editContact(input("Which contact would you like to edit? (please type only integers) "))
    elif choice == "3":
        d.close()
        f.close()
        d = open("addressBook\data.txt", "a+")
        f = open("addressBook\Book.txt", "a+")
        deleteItem(input("Which contact would you like to delete? (please type only integers) "))
    else:
        break

print("Ending...")
d.close()
f.close()
d = open("addressBook\data.txt", "a+")
f = open("addressBook\Book.txt", "a+")

writeToBook()

d.close()
f.close()