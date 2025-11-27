# A8_T5 Login and register


import hashlib
import os

FILENAME = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def load_credentials() -> list:
    users = []
    if not os.path.exists(FILENAME):
        return users

    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(DELIMITER)
                users.append(parts)
    return users


def save_user(user_id: int, username: str, password_hash: str) -> None:
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{user_id}{DELIMITER}{username}{DELIMITER}{password_hash}\n")


def register():
    users = load_credentials()
    user_id = len(users)

    username = input("Insert username: ")
    password = input("Insert password: ")

    hashed = hash_password(password)
    save_user(user_id, username, hashed)

    print("User registration completed!")


def login() -> str | None:
    users = load_credentials()

    username = input("Insert username: ")
    password = input("Insert password: ")
    hashed = hash_password(password)

    for user in users:
        if user[1] == username and user[2] == hashed:
            print("Login successful!")
            return username

    print("Invalid username or password!")
    return None


def user_menu(username: str):
    while True:
        print("User options:")
        print("1 - View profile")
        print("2 - Change password")
        print("0 - Logout")
        choice = input("Your choice: ")

        if choice == "1":
            print(f"Username: {username}")
        elif choice == "2":
            print("Password change not implemented.")
        elif choice == "0":
            break


def main():
    print("Program starting.")

    while True:
        print("Options:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            user = login()
            if user:
                user_menu(user)
        elif choice == "2":
            register()
        elif choice == "0":
            print("Exiting program.")
            break

    print("Program ending.")


if __name__ == "__main__":
    main()
