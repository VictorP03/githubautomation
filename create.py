import requests
from secrets import GITHUB_TOKEN
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--name", '-n', type=str, dest="name", required=True)
parser.add_argument("--private", '-p', dest="is_private", action="store_true")
args = parser.parse_args()
name = args.name
is_private = args.is_private

API_URL = 'https://api.github.com'
if is_private:
    jData = '{"name": "' + name + '", "private": true}'
else:
    jData = '{"name": "' + name + '", "private": false}'

headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}
try:
    r = requests.post(API_URL + "/user/repos", data=jData, headers=headers)
    r.raise_for_status()
except FileExistsError as err:
    raise SystemExit(err)

try:
    PROJECT_PATH = 'C:/projecten/'
    os.chdir(PROJECT_PATH)
    os.system("mkdir " + name)
    os.chdir(PROJECT_PATH + name)
    os.system("git init")
    os.system("git remote add origin https://github.com/VictorP03/" + name + ".git")
    os.system("echo '# " + name + "' >> README.md")
    os.system("git add .")
    os.system("git commit -m \"first commit\"")
    os.system("git push origin master")
    os.system("code .")
except FileExistsError as err:
    raise SystemExit(err)
