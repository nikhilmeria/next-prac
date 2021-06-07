from http.server import BaseHTTPRequestHandler
import json
import requests
from nsetools import Nse


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # nse = Nse()
        # q = nse.get_quote('infy', as_json=True)
        # data = json.dumps(q)

        res = requests.get("https://jsonplaceholder.typicode.com /todos")
        data = json.loads(res.text)

        self.wfile.write(
            str(data).encode())
        return
