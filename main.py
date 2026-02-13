import datetime
import json
expenses=[]

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []



def add_expense():
    
    expense = {
        "id":len(expenses)+1,
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "category": "",
        "amount": 0.0,
        "description": ""
    }
    expense["amount"] = float(input("Enter expense amount :"))
    expense["category"] = input("Enter category of expense :")
    expense["description"] = input("Write a description for expense :")
    
    expenses.append(expense)
    save_expenses()
    
    

def view_all():
    for x in expenses:
        print(x)

def view_total():
    total=0
    for x in expenses:
        total=total+x["amount"]
    print(f"the total expense is Rs {total}")
    

def cat_filter():
    category=input("Enter category :")
    for x in expenses:
        if x["category"]==category:
            print(x)


def delete_exp():
    number=int(input("Enter the id of record to delete : "))
    for x in expenses:
        if x["id"]==number:
            expenses.remove(x)
            save_expenses()
            print("Expense deleted successfully.")
            return
    print("record not found")

# main function block
def main():
    load_expenses()
    while True:
        print("===== Expense Tracker =====")
        print('''1. Add Expense
2. View All Expenses
3. View Total Expense
4. Filter by Category
5. Delete Expense
6. Exit
''')
        choice = int(input("Please Enter your choice : "))
        
        
        match choice:
            case 1:
                add_expense()
            case 2:
                view_all()
            case 3:
                view_total()
            case 4:
                cat_filter()
            case 5:
                delete_exp()
            case 6:
                print("Exit Good Bye !!")
                break
            case _:
                print("invalid choice try again")

main()
    


