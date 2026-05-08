from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        
        db_host = os.getenv("DB_HOST", "not set")
        db_name = os.getenv("DB_NAME", "not set")
        
        message = f"""
        <h1>Temu's DevOps App</h1>
        <p>App is running!</p>
        <p>Connected to database: {db_name}</p>
        <p>Database host: {db_host}</p>
        """
        self.wfile.write(message.encode())
    
    def log_message(self, format, *args):
        pass

HTTPServer(("", 5000), Handler).serve_forever()