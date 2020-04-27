import httplib2
import webbrowser
from pprint import pprint

bin_url = 'https://httpbin.org/'

webbrowser.open(bin_url)

http = httplib2.http

resp, data = http.request(bin_url,  method = 'POST')

pprint(resp)

type(resp), len(resp)

resp.status, resp.reason, resp.version

pprint(data)

type(data), len(data)

html = data.decode("UTF-8")
type(html)

pprint(html)

resp, data = http.request('http://www.google.com', method = 'HEAD')
pprint(resp)
pprint('Data After resp')
type(data)
data = data.decode('ISO-8859-1')
pprint(data)

resp, data = http.request('https://httpbin.org/get', method='GET')
pprint(resp)

post_data = '{"name": "Pranav", "College": "UMA"}'
resp, data = http.request('https://httpbin.org/post',
                    method = 'POST',
                    body = post_data,
                    headers = {'content-type': 'application/json'})

pprint(resp)


pprint(data.decode('UTF-8'))

post_data = '{"name": "Pranav", "College": "UMA"}'
resp, data = http.request('https://httpbin.org/put',
                    method = 'PUT',
                    body = post_data,
                    headers = {'content-type': 'application/json'})

pprint(resp)