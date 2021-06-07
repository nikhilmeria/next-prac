from http.server import BaseHTTPRequestHandler
from nsetools import Nse


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        nse = Nse()
        q = nse.get_quote('infy')

        self.wfile.write(
            str(q['buyPrice1']).encode())
        return
