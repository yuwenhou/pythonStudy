import time


def login():
    return "welcome.....login time:%s" % time.ctime()


def reister():
    return "welcome.....register time:%s" % time.ctime()


def profile():
    return "welcome.....profile time:%s" % time.ctime()

def application(file_name):
    if file_name == '/login.py':
        return login()
    elif file_name == "/register.py":
        return reister()
    else:
        return "not found your page..."


