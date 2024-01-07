#!/usr/bin/python3
"""A script that
- Takes in a url
- Sends a request
- displays the body of the response decoded in utf-8
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    from urllib.error import URLError, HTTPError
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('UTF-8')
            print(content)
    except HTTPError as e:
        print('Error code: ', e.code)
