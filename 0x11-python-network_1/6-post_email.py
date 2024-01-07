#!/usr/bin/python3
"""A script that
-takes in a url and an email address
-sends a post request to the passed url with the email as a parameter
-displays the body of the response
"""

if __name__ == '__main__':
    import requests
    import sys

    r = requests.post(sys.argv[1], data = {'email': sys.argv[2]})
    print(r.headers.get('X-Request-Id')
