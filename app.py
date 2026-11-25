import os
import datetime
import logging

from flask import Flask, request

app = Flask(__name__)

MESSAGE = os.environ.get("APP_MESSAGE", "AI app запущено")
PORT = int(os.environ.get("APP_PORT", "8000"))

import os as _os
_os.makedirs("/app/logs", exist_ok=True)

logging.basicConfig(
    filename="/app/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


@app.route("/")
def index():
    logging.info("запрос GET / от %s", request.remote_addr)
    return (
        f"<h1>{MESSAGE}</h1>"
        f"<p>время: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}</p>"
        f"<p>порт: {PORT}</p>"
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
# minor change
# edit
# правка app.py
