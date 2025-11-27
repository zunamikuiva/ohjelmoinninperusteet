import hashlib

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    return hashlib.md5(password.encode()).hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    user_id = 0

    try:
        with open(CREDENTIALS_FILE, "r") as file:
            user_id = sum(1 for _ in file)
    except FileNotFoundError:
        user_id = 0

    hashed = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{user_id}{DELIMITER}{PUsername}{DELIMITER}{hashed}\n")


def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    hashed = hash_password(PPassword)

    try:
        with open(CREDENTIALS_FILE, "r") as file:
            for line in file:
                user_id, username, stored_hash = line.strip().split(DELIMITER)
                if username == PUsername and stored_hash == hashed:
                    return True
    except FileNotFoundError:
        pass

    return False


def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    try:
        with open(CREDENTIALS_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(DELIMITER)
                if parts[1] == PUsername:
                    return parts
    except FileNotFoundError:
        pass

    return []


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    new_hash = hash_password(PNewPassword)
    updated_lines = []

    try:
        with open(CREDENTIALS_FILE, "r") as file:
            for line in file:
                user_id, username, stored_hash = line.strip().split(DELIMITER)

                if username == PUsername:
                    updated_lines.append(f"{user_id}{DELIMITER}{username}{DELIMITER}{new_hash}\n")
                else:
                    updated_lines.append(line)
    except FileNotFoundError:
        return

    with open(CREDENTIALS_FILE, "w") as file:
        file.writelines(updated_lines)
