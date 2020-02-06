import time
import sys


def mac_ani(t):
    while t > 0:
        sys.stdout.write('\rSure : {} saniye '.format(t))
        t -= 1
        sys.stdout.flush()
        time.sleep(1)

sonuc = mac_ani(90)
print(sonuc)