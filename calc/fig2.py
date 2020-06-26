from cgi import parse_qs
from template2 import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    x = d.get('x', [''])[0]
    y = d.get('y', [''])[0]
    sum,product = 0,0 

    if '' not in [x,y]:
        x,y = int(x), int(y)
        response_body = html % {
            'sum': x+y,
            'product': x*y,
        }
	
    start_response('200 OK',[
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]

