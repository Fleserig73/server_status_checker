import argparse
from http.client import HTTPSConnection

def status_check(url):
    conn = HTTPSConnection(url)
    conn.request("GET", "/")
    response = conn.getresponse()
    return response.status, response.reason


parser = argparse.ArgumentParser(description='Server Status Checker')

parser.add_argument('--url', type=str,
                    help='enter url')
args = parser.parse_args()


if args.url is None:
    url = input("Write url:   ")
else:
    url = args.url

print(" - ".join(map(str,status_check(url))))
