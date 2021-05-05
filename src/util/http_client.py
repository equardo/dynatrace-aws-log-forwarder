import ssl
import time
import urllib.error
import urllib.request

from util.logging import log_multiline_message

TIMEOUT_SEC = 10


def perform_http_request_for_json(url, encoded_body_bytes, method, headers, verify_SSL: bool):
    start_time = time.time()

    print(f"Performing {method} call for URL {url}")

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    if verify_SSL:
        ssl_context.verify_mode = ssl.CERT_REQUIRED
    else:
        ssl_context.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(
        url,
        encoded_body_bytes,
        headers,
        method=method
    )

    duration = time.time() - start_time
    duration = round(duration, 2)

    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=TIMEOUT_SEC) as response:
            status = response.code
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        status = e.code
        # body = e.read().decode("utf-8")
        body = e.read().decode()

    log_multiline_message(f"Response: call duration {duration}s, status code {status}, body '{body}'")
    return status, body