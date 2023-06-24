import bcrypt
from datetime import datetime

__salt = b'$2b$12$.SNNRQd0neb/k4DfuujBGu'

def log(type, msg):
    if type == "info":
        print("[INFO] " + msg)
    elif type == "err":
        print("[ERROR] " + msg)
    elif type == "warn":
        print("[WARNING] " + msg)
    elif type == "scss":
        print("[SUCCESS] " + msg)
    elif type == "log":
        print("[LOG] " + msg)
    elif type == "load":
        print("[LOADING] " + msg)
    else:
        print("[UNKNOWN] " + msg)

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), __salt)
    return hashed

def check_password(password, hashed):
    new_pass = hash_password(password)
    pass_hash = "b'" + hashed + "'"
    if str(new_pass) == str(pass_hash):
        return True
    else:
        return False

def Check_Birthday(birthday):
    try:
        fecha = datetime.strptime(birthday, "%d/%m/%Y")
        return True
    except ValueError:
        return False