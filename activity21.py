#adding and deleting

name_list={}

def add(name,surname):
    name_list[name] = surname
    print(f"{name} was added")

def del_name(name):
    if name in name_list:
        del name_list[name]
        print(name_list)

    else:
        print(f"{name} is not found")

def display_names():
    print(name_list)


def main():
    while True:
       try:
           
           user = int(input("press 1 to add press 2 to delete press 3 to view list: "))

           if user == 1:
               name = input("Enter your name: ")
               surname = input("enter surname: ")
               add(name,surname)


           elif user == 2:
               name = input("Enter name you wish to remove: ")
               del_name(name)

           elif user == 3:
               display_names()

           

       except ValueError:
           print("ivalid input")


if __name__ == "__main__":
  main()

