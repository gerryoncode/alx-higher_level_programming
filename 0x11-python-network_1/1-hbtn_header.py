#!/usr/bin/python3
"""
Takes the URL as an arg, sends the request and displays the value of X-Request-Id on
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    if len(sys.argv) < 1:
        print("Usage: Script requires atleast 1 argument")
        sys.exit(1)

    arg1 = sys.argv[1]

    with urllib.request.urlopen(arg1) as response:
        content = response.read()
        info = response.info()
        print(info["X-Request-Id"])

