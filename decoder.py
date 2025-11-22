import sys
import base64

ct = base64.urlsafe_b64decode(sys.argv[1])
msg = bytearray(c1 ^ c2 for c1, c2 in zip(ct[:16], ct[16:]))
n = msg[0]
print(msg[1: n + 1].decode())

