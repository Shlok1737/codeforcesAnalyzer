import requests
import json

userName = "tourist"

url = "https://codeforces.com/api/user.status"
params = {
    "handle": userName
}

response = requests.get(url, params=params)

data = response.json()
# data contains all submissions made by the user tourist

submission = data["result"][0]

problem = submission["problem"]

print(problem["name"])

if "rating" in problem:
    print(problem["rating"])
else:
    print("No rating")

print(problem["tags"])

solved = []

for sub in data["result"]:
    if sub["verdict"] == "OK":
        solved.append(sub)

# print(len(solved))

unique = {}

for sub in solved:
    prob = sub["problem"]
    pk = (prob["contestId"], prob["index"])
    unique[pk] = prob # if key already exists, it overwrites (hence no duplicates)
    # pk = key and prob = value

problems = list(unique.values()) #.values() returns all the value in the dict it is used on
# print(len(problems))


new_data = []

for p in problems:
    new_data.append({
        "name": p["name"],
        "rating": p.get("rating", 0),
        "tags": p["tags"]
    })
# new data contains all unique problems' data (only name, rating and tags)

with open("solved.json", "w") as f:
    json.dump(new_data, f, indent=2)
f.close()
