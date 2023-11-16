import argparse
import requests

def status_check(url):
    response = requests.get(url)
    return response.status_code

parser = argparse.ArgumentParser(description='Server Status Checker')
parser.add_argument('--url', type=str,
                    help='enter url')
args = parser.parse_args()

if args.url is None:
    url = input("Write url:   ")
else:
    url = args.url

print(status_check(url))
