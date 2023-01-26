from cryptography.fernet import Fernet

''' For creating random number of key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
# We created key using this function and stored in key.key

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt")as f:
        for words in f.readlines():
            data = words.strip()
            user, password = data.split("|")
            print("User:", user, "| Password : ",
                  fer.decrypt(password.encode()).decode())


def add():
    name = input("Accont name : ")
    pwd = input("Password : ")

    with open("passwords.txt", "a")as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:

    mode = input(
        "Whould you like to add new password or veiw exitsting ones (view, add), press q for quit : ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Inapropriate type please try again!")
