# from functions import find_actor , actors
import requests, pprint

pp = pprint.PrettyPrinter(indent=4)

def github_status():
    github_status = requests.get('https://www.githubstatus.com/api/v2/status.json')
    status_r = github_status.json()
    return status_r['status']['description']

print(github_status())
