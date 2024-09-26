employees_list = {}

def add(name,salary):
    employees_list[name] = salary
    print(f"{name}  is added")

def display():
    print(employees_list)

def delete(name):
    if name in employees_list:
        del employees_list[name]
        print(employees_list)

    else:
        print("employee not found")

def high_salary():
    x = max(employees_list,key=employees_list.get)
    print(x)

    

def main():
    while True:
        try:
            user = int(input("press 1 add,press 2 to view list,press 3 to remove,press 4 to get high salary: "))

            

            if user == 1:
                name = input("Enter employees name: ")
                salary = float(input("Enter employees salary: "))
                add(name,salary)

            elif user == 2:
              
                display()

            elif user == 3:
                name = input("Enter name: ")
                delete(name)

            elif user == 4:
                high_salary()


            


        except ValueError:
            print("invalid input")



if __name__ =="__main__":
    main()