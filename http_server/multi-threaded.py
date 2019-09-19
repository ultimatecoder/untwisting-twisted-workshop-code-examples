import time

from http import server
from socketserver import ThreadingMixIn


class RequestHandler(server.SimpleHTTPRequestHandler):

    def do_GET(self):
        start_time = time.time()
        time.sleep(5)
        end_time = time.time()
        self.send_response(200, "OK")
        self.end_headers()
        response = (
            "Started at {}, Ended at {} difference {}".format(
                start_time, end_time, end_time - start_time
            )
        )
        self.wfile.write(response.encode("utf-8"))
        return


class ThreadedHTTPServer(ThreadingMixIn, server.HTTPServer):
    deamon_threads = True

if __name__ == "__main__":
    with ThreadedHTTPServer(
        ('localhost', 8000), RequestHandler
    ) as http_server:
        http_server.serve_forever()
