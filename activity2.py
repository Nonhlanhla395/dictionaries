employees = [
    {
        "name": "Andiswa",
        "salary": 12000
    },
    {
        "name": "Luvuyo",
        "salary": 15000
    },
    {
        "name": "Sandiswa",
        "salary": 10000
    },
    {
        "name": "Amahle",
        "salary": 20000
    }
]

def add():
  name= input("Enter name: ")
  salary = int(input("Enter salary: "))
  employees[name] = salary