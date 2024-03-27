from cryptography.fernet import Fernet


def load_key_and_master_pwd():
    with open("key.key", "rb") as f:
        key = f.read()
    master_pwd = input("Enter your master password: ")
    return key + master_pwd.encode()


fer = Fernet(load_key_and_master_pwd())


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"Username: {user}, Password: {fer.decrypt(pwd.encode()).decode()}")


def add():
    name = input("Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {fer.encrypt(pwd.encode()).decode()}\n")


while True:
    mode = input("Would you like to 'add' or 'view' your password? ").lower()
    if mode == "q":
        break

    locals()[mode]()
