import json, os, sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "db", "incidents.db")
SEVERITIES = {"LOW", "MEDIUM", "HIGH"}

class H(BaseHTTPRequestHandler):
    def reply(self, code, obj):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode())

    def do_GET(self):
        if self.path != "/incidents":
            return self.reply(404, {"error": "unknown address"})
        db = sqlite3.connect(DB)
        rows = db.execute("SELECT id, title, severity, status FROM incidents").fetchall()
        db.close()
        self.reply(200, [{"id": r[0], "title": r[1], "severity": r[2], "status": r[3]} for r in rows])

    def do_POST(self):
        if self.path != "/incidents":
            return self.reply(404, {"error": "unknown address"})
        try:
            n = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(n))
            title = data["title"].strip()
            severity = data["severity"]
            assert title and severity in SEVERITIES
        except Exception:
            return self.reply(400, {"error": "bad incident"})
        db = sqlite3.connect(DB)
        cur = db.execute("INSERT INTO incidents (title, severity) VALUES (?, ?)", (title, severity))
        db.commit()
        new_id = cur.lastrowid
        db.close()
        self.reply(201, {"id": new_id, "title": title, "severity": severity, "status": "OPEN"})

print("backend on http://localhost:9001", flush=True)
HTTPServer(("localhost", 9001), H).serve_forever()
