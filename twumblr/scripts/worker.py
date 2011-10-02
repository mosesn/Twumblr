#!/usr/bin/env python

import sys
import time
import signal

# Callback called when you run `supervisorctl stop'
def sigterm_handler(signum, frame):
    print >> sys.stderr, "Kaboom Baby!"
    sys.exit(0)

def main():
    while True:
        print >> sys.stderr, "Tick"
        time.sleep(1)

# Bind our callback to the SIGTERM signal and run the daemon:
if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sigterm_handler)
    main()
