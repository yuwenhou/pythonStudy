def application(environ, start_response):
    start_response('200 OK',[('Content-Type','text/html;charset=utf-8',)])
    return 'Hello world! 为什么不能出现中文'