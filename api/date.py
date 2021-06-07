from http.server import BaseHTTPRequestHandler
import json
from nsetools import Nse


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        nse = Nse()
        q = nse.get_quote('infy')
        data = json.dumps(q)

        self.wfile.write(
            str(type(data)).encode())
        return
