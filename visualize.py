import json
import matplotlib.pyplot as plt

with open("solved.json", "r") as f:
    problems = json.load(f)

tag_count = {}

for p in problems:
    for tag in p["tags"]:
        if tag not in tag_count:
            tag_count[tag] = 0

        tag_count[tag] += 1

tags = list(tag_count.keys())
counts = list(tag_count.values())

plt.figure(figsize=(12, 6))
plt.bar(tags, counts)
plt.xticks(rotation=90) #tags overlap if kept horizontal
plt.tight_layout()
plt.show()
