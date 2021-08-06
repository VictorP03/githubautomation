import requests
from pprint import pprint
from secrets import GITHUB_TOKEN
import argparse

API_URL = 'https://api.github.com'
jData = '{"name":"name"}'
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}
r = requests.post(API_URL + "/user/repos", data=jData, headers=headers)

pprint(r.json())