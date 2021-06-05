from http.server import BaseHTTPRequestHandler
from datetime import datetime
from nsetools import Nse


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        nse = Nse()
        # q = nse.get_quote('infy')
        self.wfile.write(
            str(nse.active_equity_monthly_url).encode())
        return
