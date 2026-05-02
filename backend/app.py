from http.server import HTTPServer, BaseHTTPRequestHandler
import signal
import sys

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), AppHandler)
    
    def handle_shutdown(signum, frame):
        print("\n[Backend] Получен сигнал остановки. Завершаю работу...")
        server.shutdown()
        sys.exit(0)

    signal.signal(signal.SIGTERM, handle_shutdown)
    signal.signal(signal.SIGINT, handle_shutdown)
    
    print("[Backend] Запущен на 0.0.0.0:8080")
    server.serve_forever()
