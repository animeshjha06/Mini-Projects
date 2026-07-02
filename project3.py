def is_empty(people):
    if len(people) == 0:
        return True
    else:
        return False
    
def add_people():
    name = input("Enter the name : ").lower()
    age = input("Enter the age : ")
    email = input("Enter the email : ").lower()

    entry = {'name' : name , "age" : age , "email":email}
    return entry

def delete_person(people):
    for i,person in enumerate(people):
        print(i+1, '-',person["name"],"|",person["age"],"|",person["email"])
    
    print()
    while True:
        number  = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range")
            else:
                people.pop(number - 1)
                break
        except:
            print("Invalid number")
        

def search_person(people):
    person_name = input("Enter the name : ").lower()
    
    for temp in people : 
        if temp['name'] == person_name:
            print("Person found!")
            print(temp['name'],temp['age'],temp['email'])
            return
        
    print("Person not found!!")


print("Welcome to people management system !! ")
print()

people = []

while True:
    commad = input("You can 'Add','Delete','Search','View' and 'Q' for quit : ").lower()

    if commad == 'add':
        person = add_people()
        people.append(person)
        print("Person is added")
    elif commad == "delete":
        if is_empty(people):
            print("List is empty!!")
        else:
            delete_person(people)
            print("Person deleted")
            print("Remainings entries : ",len(people))
    elif commad == 'search':
        if is_empty(people):
            print("List is empty!!")
        else:
            search_person(people)
    elif commad == 'view':
        if is_empty(people):
            print("List is empty!!")
        else:
            print("Complete list : ")
            for i in people:
                print(i)
    elif commad == 'q':
        break
    else:
        print("Invalid input, try again")