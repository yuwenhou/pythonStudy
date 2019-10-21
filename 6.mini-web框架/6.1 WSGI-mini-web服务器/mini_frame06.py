def index():
    return "这是主页"

def login():
    return "居然点到登陆页了"


def application(environ, start_response):
    start_response('200 OK',  [('Content-Type', 'text/html;charset=utf-8',)])
    file_name = environ['PATH_INFO']
    if file_name == '/index.py':
        return index()
    elif file_name == '/login.py':
        return login()
    else:
        return 'Hello world! 为什么不能出现中文'