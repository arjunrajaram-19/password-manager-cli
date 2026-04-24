def menu():
    print("\n1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Delete Account")
    print("5. Show Password")
    print("6. Exit")

def load_passwords():
    try:
        with open("passwords.txt", "r") as f:
            lines=f.readlines()
        data=[]
        for line in lines:
            parts=line.strip().split(",")
            if len(parts)!=3:
                continue
            data.append([parts[0], parts[1], parts[2]])
        return data
    except:
        return []

def save_passwords(data):
    with open("passwords.txt", "w") as f:
        for item in data:
            f.write(item[0]+","+item[1]+","+item[2]+"\n")
    
def add_account(data):
    website=input("Enter website: ").strip().lower()
    if website=="":
        print("Website cannot be empty")
        return
    username=input("Enter username: ").strip()
    if username=="":
        print("Username cannot be empty")
        return
    password=input("Enter password: ").strip()
    if password=="":
        print("Password cannot be empty")
        return
    for item in data:
        if item[0] == website and item[1] == username:
            print("Account already exists")
            return
    data.append([website, username, password])
    save_passwords(data)
    print("Account added")

def view_accounts(data):
    if not data:
        print("No accounts found")
        return
    for i in range(len(data)):
        masked = "*" * len(data[i][2])
        print(str(i+1)+". "+data[i][0]+" - "+data[i][1]+" - "+masked)

def search_account(data):
    if not data:
        print("No accounts found")
        return
    website=input("Enter website: ").strip().lower()
    found=False
    for item in data:
        if item[0]==website:
            masked="*"*len(item[2])
            print(item[0]+" - "+item[1]+" - "+masked)
            found=True
    if not found:
        print("Not found")

def delete_account(data):
    view_accounts(data)
    if not data:
        return
    try:
        index=int(input("Enter number to delete: "))-1
    except ValueError:
        print("Invalid input")
        return
    if 0<=index<len(data):
        confirm=input("Are you sure? (y/n): ")
        if confirm.lower()!="y":
            print("Cancelled")
            return
        data.pop(index)
        save_passwords(data)
        print("Deleted")
    else:
        print("Invalid index")

def show_password(data):
    if not data:
        print("No accounts found")
        return
    website=input("Enter website: ").strip().lower()
    username=input("Enter username: ").strip()
    for item in data:
        if item[0]==website and item[1]==username:
            confirm=input("Show password? (y/n): ")
            if confirm.lower()!="y":
                print("Cancelled")
                return
            print("Password:", item[2])
            return

    print("Account not found")

data = load_passwords()
while True:
    menu()
    choice=input("Choose: ")
    if choice=="1":
        add_account(data)
    elif choice=="2":
        view_accounts(data)
    elif choice=="3":
        search_account(data)
    elif choice=="4":
        delete_account(data)
    elif choice=="5":
        show_password(data)
    elif choice=="6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")