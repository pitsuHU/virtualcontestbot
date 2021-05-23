import requests

res = requests.get('https://codeforces.com/api/contest.list?gym=false')
Data = res.json()
Data = Data['result']

contest_list = {}

for x in Data:
    contest_list[x['id']] = x['name']
    if x['name']
