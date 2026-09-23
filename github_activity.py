import urllib.request
import sys
import json
import ast 

user = sys.argv[1]
url = f"https://api.github.com/users/{user}/events"

with urllib.request.urlopen(url) as response:
    raw_data = response.read()
data = raw_data.decode("utf-8")
data = json.loads(data)

result = []
for d in data:
    if d["type"] == "PushEvent":
        repo_name = d["repo"]["name"]
        string = f"Pushed commits to {repo_name}"
        found = False
        for r in result:
            if r[0] == string:
                r[1] += 1
                found = True
                break
        if not found:
            result.append([string, 1])

for r in result:
    print(r)
    
