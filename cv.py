product_list= {}

def Add_product(name,price):
    product_list[name] = price
    print(f"you have added {name} product")

def display_product():
    print(product_list)

def del_product(name):
    if name in product_list:
        del product_list[name]
        print(product_list)

    else:
        print(f"{name} is not found!")

def  product_price(price):
    for i in product_list.items():
        if price in i :
            print(i[0])

    

def main():
    while True:
        try:
            user  = int(input("press 1 to add ,press 2 to view all product, press 3 to remove product, press 4 to view products with same price:  "))

            if user == 1:
                name = input("Enter product name: ")
                price = float(input("Enter price:"))
                Add_product(name,price)

            elif user == 2:
                display_product()

            elif user == 3:
                name = input("Enter product name you wish to remove: ")
                del_product(name)

            elif user == 4:
                price = float(input("Enter price: "))
                product_price(price)


            
        except ValueError:
            print("invalid input")

if __name__=="__main__":
    main()